from fastapi import APIRouter

router = APIRouter()


@router.get('/auth/')
def users():
    return {"user": "auth"}
