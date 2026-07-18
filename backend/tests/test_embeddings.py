import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from rag.embeddings import get_embedding_model

embedding_model = get_embedding_model()

text = "Apple designs and manufactures consumer electronics."

embedding = embedding_model.embed_query(text)

print("=" * 60)
print("EMBEDDING TEST")
print("=" * 60)

print(f"Embedding Dimension: {len(embedding)}")

print("\nFirst 10 Values:\n")
print(embedding[:10])