from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "System info logging every 10 seconds"}
