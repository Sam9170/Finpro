from sqlmodel import SQLModel, Field
from typing import Optional

class Bank(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    bank_name: str
    account_number: str
    balance: float
