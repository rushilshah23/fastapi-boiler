import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from common.utils.logger import get_logger

logger = get_logger(__name__)

class JSONLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = None
        try:
            response = await call_next(request)
            process_time = round(time.time() - start_time, 4)

            logger.info({
                "event": "http_request",
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "client": request.client.host if request.client else None,
                "duration": process_time,
            })

            return response
        except Exception as e:
            process_time = round(time.time() - start_time, 4)
            logger.error({
                "event": "http_error",
                "method": request.method,
                "path": request.url.path,
                "error": str(e),
                "duration": process_time,
            })
            raise
