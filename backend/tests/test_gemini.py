import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gemini.gemini_client import ask_gemini

answer = ask_gemini(
    "Should I invest in NVIDIA?",
    "NVIDIA has shown strong AI-driven revenue growth over the last few quarters."
)
print(answer)