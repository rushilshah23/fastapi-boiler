from fastapi import Response
from common.configs.env import CommonConfig


def set_cookie(key:str, value:str,max_age:int, response:Response):
    response.set_cookie(
    key=key,
    value=value,
    httponly=CommonConfig.COOKIE_HTTP_ONLY,
    samesite=CommonConfig.COOKIE_SAMESITE,  # Lax is okay too, Strict is safest
    secure=CommonConfig.COOKIE_SECURE,        # HTTPS only
    max_age=max_age
)
