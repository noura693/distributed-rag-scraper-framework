from datetime import datetime

document_history = {}


def store_version(url, content):

    if url not in document_history:
        document_history[url] = []

    version = {
        "timestamp": datetime.now().isoformat(),
        "content": content
    }

    document_history[url].append(version)


url = "https://quotes.toscrape.com/"

store_version(
    url,
    "Distributed scraping with Celery workers"
)

store_version(
    url,
    "Distributed scraping with Celery workers and Redis"
)

store_version(
    url,
    "Distributed scraping with Celery workers, Redis and Qdrant"
)

for index, version in enumerate(
    document_history[url],
    start=1
):
    print(f"Version {index}")
    print(version["timestamp"])
    print(version["content"])
    print("-" * 40)