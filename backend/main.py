from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import sqlite3

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# Define request schema
class QueryRequest(BaseModel):
    query: str

# POST endpoint for natural language to SQL
@app.post("/query")
def generate_sql(request: QueryRequest):
    user_input = request.query

    # Prompt for OpenAI
    prompt = f"Convert this natural language to SQL: {user_input}"

    # Get completion from OpenAI
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100
    )

    sql_query = response.choices[0].text.strip()

    # Optional: Execute SQL on local database
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()

    return {
        "sql": sql_query,
        "results": results
    }
