# fastapi-ip-rate-limit-sliding

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-ip-rate-limit-sliding/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

High-precision sliding-window rate limiter dependency for FastAPI with automatic IP extraction and standard 429 headers.

---

## 🚀 Features

- ⏱️ **Sliding Window Counter**: Smooth rate limiting without reset boundary spikes.
- 🌐 **Proxy & Cloudflare Aware**: Accurately extracts client IP from `CF-Connecting-IP` and `X-Forwarded-For`.
- 🪶 **Zero External Dependencies**: Pure Python in-memory data structure.

---

## 📦 Installation

```bash
pip install fastapi-ip-rate-limit-sliding
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI, Depends
from fastapi_ip_rate_limit_sliding import SlidingRateLimiter

app = FastAPI()
limiter = SlidingRateLimiter(limit=10, window_seconds=60)

@app.get("/api/data", dependencies=[Depends(limiter)])
def get_data():
    return {"status": "success"}
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this rate limiter protected your APIs, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
