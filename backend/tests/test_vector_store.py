import sys
from pathlib import Path

# Add backend directory to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from rag.pdf_loader import extract_text_from_pdf
from rag.chunking import chunk_text
from rag.vector_store import create_vector_store

# PDF location
pdf_path = "uploads/apple_2024.pdf"

# Step 1: Extract text
text = extract_text_from_pdf(pdf_path)

# Step 2: Split into chunks
chunks = chunk_text(text)

# Step 3: Limit chunks for testing (avoids Gemini free-tier rate limit)
MAX_CHUNKS = 50
chunks = chunks[:MAX_CHUNKS]

print("=" * 60)
print("VECTOR STORE TEST")
print("=" * 60)
print(f"Total Chunks to Store: {len(chunks)}")

# Step 4: Create vector database
db = create_vector_store(chunks)

print("\n✅ Vector store created successfully!")

print("\nDatabase Location:")
print("data/chroma")

print("\nSample Chunk:")
print("-" * 60)
print(chunks[0][:500])
print("-" * 60)