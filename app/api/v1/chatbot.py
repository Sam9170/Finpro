from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def chatbot():
    return {"reply": "This is a dummy chatbot response."}
