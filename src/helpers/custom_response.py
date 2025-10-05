from fastapi.responses import JSONResponse
from typing import Any, Optional, Dict
import datetime
import uuid


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
        # Standard response body
        body = {
            "status": status,
            "status_code": status_code,
            "message": message,
            "data": data,
            "error": error,
            "meta": {
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "request_id": str(uuid.uuid4()),
                **(meta or {})
            }
        }

        super().__init__(content=body, status_code=status_code, headers=headers)
