from fastapi import Response
from common.configs.env import CommonConfig
from typing import Optional

class CookieUtils:
    @staticmethod
    def set_cookie(
        key: str,
        value: str,
        response: Response,
        max_age: Optional[int] = None,
        path: str = "/",
        domain: Optional[str] = None,
        secure: Optional[bool] = None,
        httponly: Optional[bool] = None,
        samesite: Optional[str] = None,
    ):
        """
        Set a cookie on the response with full metadata.

        If secure/httponly/samesite are None, defaults from CommonConfig are used.
        """
        response.set_cookie(
            key=key,
            value=value,
            max_age=max_age,
            path=path,
            domain=domain,
            secure=secure if secure is not None else CommonConfig.COOKIE_SECURE,
            httponly=httponly if httponly is not None else CommonConfig.COOKIE_HTTP_ONLY,
            samesite=samesite if samesite is not None else CommonConfig.COOKIE_SAMESITE,
        )
