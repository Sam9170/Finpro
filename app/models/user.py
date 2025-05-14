from pydantic import BaseModel, EmailStr, Field

class UserDetails(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    phone: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip: str = Field(...)
    country: str = Field(...)

class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
