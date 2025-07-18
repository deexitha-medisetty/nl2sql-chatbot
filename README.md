\# 🧠 NL2SQL Chatbot



A FastAPI + OpenAI-powered chatbot that converts natural language questions into executable SQL queries.



\## 💡 Features

\- Natural language → SQL using OpenAI

\- SQLite database querying

\- FastAPI backend with Swagger UI



\## 🚀 Getting Started



```bash

git clone https://github.com/deexitha-medisetty/nl2sql-chatbot.git

cd nl2sql-chatbot

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

cd backend

python setup\_db.py

uvicorn main:app --reload



