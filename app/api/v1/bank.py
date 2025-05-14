from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_bank_accounts():
    return {"banks": []}
