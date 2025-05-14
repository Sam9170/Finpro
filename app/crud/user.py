from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.db_user import User
from app.models.user import UserDetails


def create_user(db: Session, user_data: UserDetails):
    """
    Create and save a new user to the database.
    Returns the created user object or None if the email already exists.
    """
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,
        phone=user_data.phone,
        city=user_data.city,
        state=user_data.state,
        zip=user_data.zip,
        country=user_data.country
    )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return None


def get_user_by_email(db: Session, email: str):
    """
    Fetch a single user by email.
    Returns the User object or None if not found.
    """
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    """
    Return a list of all users in the database.
    """
    return db.query(User).all()


def delete_user_by_email(db: Session, email: str) -> bool:
    """
    Deletes a user by their email address.
    Returns True if the user was deleted, False if not found.
    """
    user = get_user_by_email(db, email)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
