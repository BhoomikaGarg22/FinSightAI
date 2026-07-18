import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from rag.retriever import get_retriever

print("=" * 60)
print("RETRIEVER TEST")
print("=" * 60)

query = "What are Apple's business risks?"

retriever = get_retriever()

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} chunks.\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print(doc.page_content[:700])
    print()