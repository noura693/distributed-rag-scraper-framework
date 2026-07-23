from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from sentence_transformers import SentenceTransformer

client = QdrantClient(
    host="localhost",
    port=6333
)

collection_name = "documents"

client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text = "Distributed scraping with Celery workers"

vector = model.encode(text).tolist()

client.upsert(
    collection_name=collection_name,
    points=[
        PointStruct(
            id=1,
            vector=vector,
            payload={
                "text": text
            }
        )
    ]
)

print("Vector stored successfully!")