from datetime import datetime, timedelta, timezone
import jwt
from typing import Dict
from config import settings


def create_access_token(data: Dict[str, str]) -> str:
    to_encode = data.copy()
    time = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expire)
    to_encode.update({"exp": time})
    encoded_jwt = jwt.encode(to_encode,
                             settings.jwt_secret,
                             algorithm=settings.jwt_algorithm)
    return encoded_jwt


def decode_access_token(token: str, key: str) -> str:
    try:
        decoded_token = jwt.decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
        return decoded_token.get(key)
    except Exception:
        return {"error": "Bad token"}
