
import os
import time

from backend.rag.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import errors

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

    max_retries = 3

    for attempt in range(max_retries):

        try:
            response = client.models.generate_content(
                model="models/gemini-3.5-flash",
                contents=prompt
            )

            return response.text

        except errors.APIError as e:

            if e.code in [429, 500, 503, 504]:

                if attempt < max_retries - 1:
                    time.sleep(2 ** (attempt + 1))
                    continue

                return (
                    "Gemini AI is temporarily unavailable due to "
                    "high demand. Please try again in a few moments."
                )

            return f"Gemini API Error: {e}"

    return "Unable to generate a response. Please try again."
