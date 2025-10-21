from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from src.helpers.custom_response import CustomResponse


sample_api = FastAPI()


@sample_api.get("/")
async def get_endpoint():
    return CustomResponse.success(message="Sample endpoint success",status_code=status.HTTP_200_OK)