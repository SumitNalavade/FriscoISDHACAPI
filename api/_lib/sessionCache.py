import os
import json
import requests
import hashlib
from upstash_redis import Redis

UPSTASH_REDIS_URL = os.environ["KV_REST_API_URL"]
UPSTASH_REDIS_TOKEN = os.environ["KV_REST_API_TOKEN"]

redis = Redis(url=UPSTASH_REDIS_URL, token=UPSTASH_REDIS_TOKEN)

def _session_key(username: str, password: str) -> str:
    """
    Create a stable, non-reversible fingerprint for (username + password).
    If the password changes, the key changes automatically.
    """
    fp = hashlib.sha256(f"{username}:{password}".encode()).hexdigest()[:16]
    return f"session:cookies:{username}:{fp}"

def save_session_cookies(username, password, session):
    try:
        cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
        
        key = _session_key(username, password)
        redis.set(key, json.dumps(cookies_dict), ex=300)
    except Exception:
        pass

def get_session_cookies(username, password):
    try:
        key = _session_key(username, password)
        cookies = redis.get(key)

        if not cookies:
            return None
        
        if isinstance(cookies, (bytes, bytearray)):
            cookies = cookies.decode("utf-8")

        cookies = json.loads(cookies)

        return cookies
    except:
        pass