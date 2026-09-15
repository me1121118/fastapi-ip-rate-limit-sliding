import pytest
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from fastapi_ip_rate_limit_sliding import SlidingRateLimiter

def test_sliding_rate_limiter():
    app = FastAPI()
    limiter = SlidingRateLimiter(limit=2, window_seconds=10)

    @app.get("/items", dependencies=[Depends(limiter)])
    def read_items():
        return {"items": [1, 2, 3]}

    client = TestClient(app)
    assert client.get("/items").status_code == 200
    assert client.get("/items").status_code == 200
    res_limited = client.get("/items")
    assert res_limited.status_code == 429
    assert "Retry-After" in res_limited.headers
