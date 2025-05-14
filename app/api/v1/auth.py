from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import UserDetails, UserLogin
from app.db.session import SessionLocal
from app.crud import user

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    """
    Dependency to get a DB session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user_data: UserDetails, db: Session = Depends(get_db)):
    """
    Register a new user.
    Returns user info on success or raises an error if the email is already used.
    """
    existing_user = user.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = user.create_user(db, user_data)
    if not new_user:
        raise HTTPException(status_code=500, detail="Failed to create user")

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "phone": new_user.phone,
            "city": new_user.city,
            "state": new_user.state,
            "zip": new_user.zip,
            "country": new_user.country,
        }
    }


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    Log in a user.
    Returns a welcome message if credentials are valid.
    """
    db_user = user.get_user_by_email(db, user_data.email)
    
    if not db_user or db_user.password != user_data.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "message": f"Welcome back, {db_user.name}!",
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "phone": db_user.phone,
            "city": db_user.city,
            "state": db_user.state,
            "zip": db_user.zip,
            "country": db_user.country,
        }
    }
