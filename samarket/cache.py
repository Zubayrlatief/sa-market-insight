"""Simple JSON file cache so repeated runs don't hammer the data sources."""

import json
import time
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "cache"
DEFAULT_TTL = 24 * 3600  # 24 hours


def get(key: str, ttl: int = DEFAULT_TTL):
    path = CACHE_DIR / f"{key}.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    if time.time() - payload.get("_fetched_at", 0) > ttl:
        return None
    return payload.get("data")


def put(key: str, data) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{key}.json"
    path.write_text(
        json.dumps({"_fetched_at": time.time(), "data": data}, ensure_ascii=False),
        encoding="utf-8",
    )
