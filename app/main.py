from fastapi import FastAPI
from app.api.v1.auth import router as auth_router

app = FastAPI(title="FinApp")

app = FastAPI()
app.include_router(auth_router, prefix="/api/v1")
