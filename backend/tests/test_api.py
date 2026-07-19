import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from api import chat_with_ai

response = chat_with_ai("What is SIP?")
print(response)