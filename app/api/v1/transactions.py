from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_transactions():
    return {"transactions": []}
