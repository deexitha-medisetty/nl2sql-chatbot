# 🧠 NL2SQL Chatbot

A chatbot that converts natural language to SQL using OpenAI and FastAPI.

## 🚀 Features
- FastAPI backend
- OpenAI GPT for query generation
- SQLite database
- Swagger UI to test API

## 🛠️ Tech Stack
- Python
- FastAPI
- SQLite
- OpenAI API

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/nl2sql-chatbot.git

# Navigate into the backend folder
cd nl2sql-chatbot/backend

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Add your .env file
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx

# Run the app
uvicorn main:app --reload
