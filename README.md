# 💸 FinApp Backend

Welcome to **FinApp** — a robust, scalable personal finance tracker backend built with FastAPI and PostgreSQL. This API powers real-time finance tracking, user management, and budgeting logic, designed for modern full-stack finance applications.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-FFD43B?style=for-the-badge&logo=python)

## 🚀 Tech Stack

### Core Components
- **Backend Framework**: FastAPI
- **Programming Language**: Python 3.12
- **ORM**: SQLAlchemy 2.0
- **Data Validation**: Pydantic v2
- **Database**: PostgreSQL
- **Task Queue**: Redis + Celery
- **Environment Management**: python-dotenv
- **API Documentation**: Swagger UI & ReDoc

## 📦 Features

### ✅ Implemented
- User registration & login via email
- PostgreSQL database integration
- Environment-based configuration (.env)
- API response validation with Pydantic
- Swagger docs at `/docs`
- Modular project structure

### 🛠️ Roadmap
| Feature | Status |
|---------|--------|
| JWT Authentication | In Progress |
| Budget tracking & summaries | Planned |
| Real-time alerts with WebSockets | Planned |
| AI-powered financial insights | Planned |
| Multi-bank account management | Planned |
| Expense analytics | Planned |

## 🏗️ Project Structure
FinApp_Backend/
│
├── app/
│   ├── api/v1/          # API routes (auth, users, etc.)
│   ├── core/            # Config & utility
│   ├── crud/            # CRUD logic (SQLAlchemy)
│   ├── db/              # Database session & models
│   ├── models/          # Pydantic schemas
│   ├── services/        # Business logic
│   ├── events/          # Redis stream/event logic
│   ├── tasks/           # Celery workers
│   ├── main.py          # Entry point
│   └── celery_worker.py
│
├── tests/               # Test cases
├── .env.example         # Environment template
├── requirements.txt     # Dependencies
└── README.md
