from fastapi import FastAPI
from app.api.v1 import auth, users, transactions, bank, insights, chatbot

app = FastAPI(title="FinApp")

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(transactions.router, prefix="/api/v1/transactions")
app.include_router(bank.router, prefix="/api/v1/bank")
app.include_router(insights.router, prefix="/api/v1/insights")
app.include_router(chatbot.router, prefix="/api/v1/chatbot")
