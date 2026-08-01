def chunk_text(text, chunk_size=100, overlap=20):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


sample_text = """
Distributed scraping with Celery workers. Redis manages task queues.
Qdrant stores vector embeddings. FastAPI provides API endpoints.

Distributed systems improve scalability and fault tolerance.
Playwright renders JavaScript websites before scraping.
Scrapy extracts structured information from webpages.

Embeddings are generated using SentenceTransformer.
Retrieved chunks are sent to FLAN-T5 for answer generation.
The final answer includes source attribution and citations.
"""

chunks = chunk_text(sample_text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 30)