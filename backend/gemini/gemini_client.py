import os
from backend.rag.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(question, context=""):
    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

User Question:
{question}
"""

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt
    )

    return response.text