# 💸 FinApp Backend

Welcome to **FinApp** — a robust, scalable personal finance tracker backend built with FastAPI and PostgreSQL. This API powers real-time finance tracking, user management, and budgeting logic, designed for modern full-stack finance applications.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-FFD43B?style=for-the-badge&logo=python)

Here's the properly formatted markdown version with all sections in correct markdown syntax, including the setup & deployment and contact sections:


## 🚀 Tech Stack

| Layer           | Technology                   |
|-----------------|------------------------------|
| **Backend**     | FastAPI, Python 3.12         |
| **Database**    | PostgreSQL                   |
| **Queue**       | Redis + Celery               |

## 📦 Features

### ✅ Implemented
- User authentication


### 🚧 Coming Soon
- AI financial insights
- Multi-currency support
- Transaction management
- Budget tracking

## ⚙️ Setup & Deployment

### Prerequisites
- Python 3.12+
- PostgreSQL 14+
- Redis server

### Installation
```bash
# Clone repository
git clone https://github.com/Sam9170/FinApp_Backend.git
cd FinApp_Backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration
1. Copy the example env file:
```bash
cp .env.example .env
```
2. Update `.env` with your credentials

### Running the Application
```bash
# Start FastAPI server
uvicorn app.main:app --reload

# Start Celery worker (in separate terminal)
celery -A app.celery_worker worker --loglevel=info
```

### Docker Deployment
```bash
docker-compose up -d --build
```

## 👨‍💻 Developer

**Sambhram Satapathy**  
- GitHub: [@Sam9170](https://github.com/Sam9170)  
- Email: [contact@example.com](mailto:contact@example.com)  
- LinkedIn: [Profile](https://linkedin.com/in/example)

## 📜 License
MIT License - See [LICENSE](LICENSE) for details.
