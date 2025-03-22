from fastapi import APIRouter

from src.lib.utils import init_logger

router = APIRouter()


@router.get("/")
def read_root():
    logger = init_logger(__name__)
    logger.info("Accessed root")
    return {"message": "System info logging every 10 seconds"}
