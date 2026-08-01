import hashlib

stored_hashes = set()


def get_content_hash(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def process_document(text):

    content_hash = get_content_hash(text)

    if content_hash in stored_hashes:
        print("Duplicate detected. Skipping.")
        return

    stored_hashes.add(content_hash)

    print("New document stored:")
    print(text)


doc1 = "Distributed scraping with Celery workers"
doc2 = "Distributed scraping with Celery workers"
doc3 = "Qdrant stores vector embeddings"

process_document(doc1)
process_document(doc2)
process_document(doc3)