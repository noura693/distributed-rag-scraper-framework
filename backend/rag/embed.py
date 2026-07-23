from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = """
Distributed scraping with Celery workers.
"""

embedding = model.encode(text)

print(len(embedding))