from dotenv import load_dotenv
import os

env_loaded = load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

print("✅ .env loaded?" , env_loaded)
print("🔑 API Key:", api_key)
