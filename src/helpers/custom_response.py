from fastapi.responses import JSONResponse
from typing import Any, Optional, Dict
import datetime
# import uuid
from asgi_correlation_id import correlation_id


class CustomResponse(JSONResponse):
    def __init__(
        self,
        status: str = "success",
        status_code: int = 200,
        message: str = "",
        data: Optional[Any] = None,
        error: Optional[Any] = None,
        meta: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.status = status
        self.status_code = status_code
        self.message = message
        self.data = data
        self._error = error
        self.meta = meta
        self._headers = headers
        
        request_id = correlation_id.get() or "N/A"

        body = {
            "status": status,
            "status_code": status_code,
            "message": message,
            "data": data,
            "error": error,
            "meta": {
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "request_id": request_id,
                **(meta or {})
            }
        }

        super().__init__(content=body, status_code=status_code, headers=headers)

    # ---------- Static Helper Methods ---------- #

    @staticmethod
    def success(message: str = "", data: Any = None, status_code: int = 200):
        """Helper to create success responses."""
        return CustomResponse(
            status="success",
            message=message,
            data=data,
            status_code=status_code
        )

    @staticmethod
    def error(message: str = "", error: Any = None, status_code: int = 400):
        """Helper to create error responses."""
        return CustomResponse(
            status="error",
            message=message,
            error=error,
            status_code=status_code
        )
        
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a CustomResponse from a dictionary (e.g., from resp.json()).
        """
        return cls(
            status=data.get("status", "success"),
            status_code=data.get("status_code", 200),
            message=data.get("message", ""),
            data=data.get("data"),
            error=data.get("error"),
            meta=data.get("meta"),
        )
