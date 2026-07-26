from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from transformers import T5Tokenizer, T5ForConditionalGeneration

client = QdrantClient(
    host="localhost",
    port=6333
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

tokenizer = T5Tokenizer.from_pretrained(
    "google/flan-t5-base"
)

llm = T5ForConditionalGeneration.from_pretrained(
    "google/flan-t5-base"
)


def answer_question(question: str):

    query_vector = embedding_model.encode(
        question
    ).tolist()

    results = client.query_points(
        collection_name="documents",
        query=query_vector,
        limit=3
    )

    sources = [
        point.payload["text"]
        for point in results.points
    ]

    context = "\n".join(sources)

    prompt = f"""
Answer the question using the provided context.

Context:
{context}

Question:
{question}
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    outputs = llm.generate(
        **inputs,
        max_new_tokens=100
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "answer": answer,
        "sources": sources
    }