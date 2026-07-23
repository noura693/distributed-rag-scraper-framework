from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

query = "distributed workers"

query_vector = model.encode(query).tolist()

results = client.query_points(
    collection_name="documents",
    query=query_vector,
    limit=3
)

for point in results.points:
    print(point.payload)
