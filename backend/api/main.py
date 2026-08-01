from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from backend.rag.rag_service import answer_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.get("/raw")
def raw_data():
    return {
        "message": "Raw scraped data endpoint",
        "data": [
            {
                "text": "Distributed scraping with Celery workers"
            }
        ]
    }


@app.get("/processed")
def processed_data():
    return {
        "message": "Processed content endpoint",
        "data": [
            {
                "cleaned_text": "Distributed scraping with Celery workers"
            }
        ]
    }


@app.get("/keyword")
def keyword_search(keyword: str):
    sample_data = [
        "Distributed scraping with Celery workers"
    ]

    results = [
        item
        for item in sample_data
        if keyword.lower() in item.lower()
    ]

    return {
        "keyword": keyword,
        "results": results
    }


@app.get("/search")
def search(query: str):

    vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name="documents",
        query=vector,
        limit=3
    )

    return [
        point.payload
        for point in results.points
    ]


@app.get("/rag")
def rag(question: str):
    return answer_question(question)