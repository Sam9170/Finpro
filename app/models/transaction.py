from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    type: str
    category: str
    amount: float
    date: datetime
    description: Optional[str]
