import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from rag.pdf_loader import extract_text_from_pdf
from rag.chunking import chunk_text

pdf_path = "uploads/apple_2024.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

print("=" * 60)
print("CHUNKING TEST")
print("=" * 60)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])