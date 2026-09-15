import time
from collections import defaultdict
from typing import Dict, List
from fastapi import HTTPException, Request, status

class SlidingRateLimiter:
    """Sliding-window rate limiter per client IP with Retry-After header."""

    def __init__(self, limit: int = 60, window_seconds: int = 60):
        self.limit = limit
        self.window_seconds = window_seconds
        self.clients: Dict[str, List[float]] = defaultdict(list)

    def _get_ip(self, request: Request) -> str:
        return (
            request.headers.get("cf-connecting-ip") or
            request.headers.get("x-forwarded-for", "").split(",")[0].strip() or
            (request.client.host if request.client else "127.0.0.1")
        )

    def __call__(self, request: Request) -> None:
        client_ip = self._get_ip(request)
        now = time.monotonic()
        cutoff = now - self.window_seconds

        history = [t for t in self.clients[client_ip] if t > cutoff]
        self.clients[client_ip] = history

        if len(history) >= self.limit:
            oldest = history[0]
            retry_after = max(1, int(self.window_seconds - (now - oldest)))
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded",
                headers={"Retry-After": str(retry_after)}
            )

        self.clients[client_ip].append(now)
