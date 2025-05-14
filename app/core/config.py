import os

class Settings:
    PROJECT_NAME: str = "FinApp"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./finapp.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")

settings = Settings()
