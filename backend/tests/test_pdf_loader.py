import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from rag.pdf_loader import extract_text_from_pdf

pdf_path = "uploads/apple_2024.pdf"

text = extract_text_from_pdf(pdf_path)

print("=" * 60)
print("PDF LOADER TEST")
print("=" * 60)
print(text[:1000])