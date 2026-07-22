from fastapi import APIRouter


router = APIRouter()


@router.get("/hello_axione")
def hello_axione() -> dict[str, str]:
    return {"msg": "Hello Axione !"}
