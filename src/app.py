from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from common.helpers.response import CustomResponse
from common.helpers.status_codes import StatusCodes
from dotenv import load_dotenv
load_dotenv(dotenv_path="./envs/.env")
from common.configs.env import CommonConfig

def create_app():
    app = FastAPI(
        docs_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION" else "/docs",
        redoc_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION"  else "/redoc",
        openapi_url=None if CommonConfig.ENVIRONMENT=="PRODUCTION"  else "/openapi.json"        
    )
    origins = CommonConfig.ALLOWED_ORIGINS

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # trusted origins
        allow_credentials=True,
        allow_methods=["*"],    # or restrict ["GET", "POST"]
        allow_headers=["*"],    # or restrict ["Authorization", "Content-Type"]
    )

    @app.get("/health")
    def health_check():
        return CustomResponse(status_code=StatusCodes.HTTP_200_OK, message=f"FAST API Boiler - {CommonConfig.ENVIRONMENT} is healthy").to_dict()
    

    return app
