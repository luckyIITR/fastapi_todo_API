from fastapi import APIRouter

route = APIRouter()


@route.get('/auth/')
def users():
    return {"user": "auth"}
