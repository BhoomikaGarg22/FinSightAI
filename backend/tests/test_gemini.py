import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gemini.gemini_client import ask_gemini

answer = ask_gemini("What is Artificial Intelligence?")

print(answer)