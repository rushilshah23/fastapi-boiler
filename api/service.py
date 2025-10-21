from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from src.helpers.custom_response import CustomResponse

from common.utils.logger import get_logger

logger = get_logger(__name__)

service_api = FastAPI()


@service_api.get("/")
async def get_endpoint():
    logger.error({"mssg":"Something is wrong"})
    return CustomResponse.success(message="Sample endpoint success",status_code=status.HTTP_200_OK)