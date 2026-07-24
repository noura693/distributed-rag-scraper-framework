from fastapi import FastAPI
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/search")
def search(query: str):
    return {
        "message": "Containerization test successful",
        "query": query
    }

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

@app.get("/search")
def search(query: str):
    return {
        "message": "Containerization test successful"
    }

("/search")
def search(query: str):

    vector = model.encode(
        query
    ).tolist()

    results = client.query_points(
        collection_name="documents",
        query=vector,
        limit=3
    )

    return [
        point.payload
        for point in results.points
    ]
