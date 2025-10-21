from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from src.helpers.custom_response import CustomResponse
from common.helpers.status_codes import StatusCodes
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "envs" / ".env"
load_dotenv(dotenv_path=ENV_PATH)

from common.configs.env import CommonConfig
from src.utils.security import SecurityHeadersMiddleware
from starlette_csrf import CSRFMiddleware 


def create_app():
    app = FastAPI(
        docs_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION" else "/docs",
        redoc_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION"  else "/redoc",
        openapi_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION"  else "/openapi.json",
        root_path="/api"       
    )
    origins = CommonConfig.ALLOWED_ORIGINS

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # trusted origins
        allow_credentials=True,
        allow_methods=["*"],    # or restrict ["GET", "POST"]
        allow_headers=["*"],    # or restrict ["Authorization", "Content-Type"]
    )
    app.add_middleware(SecurityHeadersMiddleware)
    app.add_middleware(CSRFMiddleware, secret=CommonConfig.CSRF_SECRET_KEY,cookie_name="csrf_token", header_name="X-CSRF-Token")


    router = APIRouter(prefix="/api")

    @app.get("/health")
    def health_check():
        return CustomResponse(status_code=status.HTTP_200_OK, message=f"FAST API Boiler - {CommonConfig.ENVIRONMENT} is healthy")

    
    
    from api import sample_api
    app.mount(path="/sample_api", app=sample_api)
    

    app.include_router(router=router)
    
    return app
