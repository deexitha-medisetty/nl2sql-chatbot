from dotenv import load_dotenv
import os
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

# ✅ Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Allow frontend access (CORS policy)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request body model
class QueryInput(BaseModel):
    query: str

# ✅ Health check route
@app.get("/")
def root():
    return {"message": "🚀 NL2SQL API is running!"}

# ✅ NL → SQL endpoint
@app.post("/query")
async def query_db(input: QueryInput):
    nl_query = input.query

    try:
        # ✅ FIXED: Correct method for openai>=1.0.0
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert SQL translator. Convert the user's natural language query into a valid SQL "
                        "statement for a SQLite table named 'students' with columns (name, age, department)."
                    )
                },
                {
                    "role": "user",
                    "content": f"Translate this to SQL: {nl_query}"
                }
            ]
        )
        sql_query = response.choices[0].message.content.strip()
    except Exception as e:
        return {"error": f"OpenAI failed: {str(e)}"}

    # 💾 Execute the SQL query against SQLite DB
    try:
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
        return {"sql": sql_query, "results": rows}
    except Exception as e:
        return {"sql": sql_query, "error": f"SQL Error: {str(e)}"}

