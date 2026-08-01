import hashlib

page_history = {}


def get_hash(content):
    return hashlib.sha256(
        content.encode("utf-8")
    ).hexdigest()


def crawl_page(url, content):

    new_hash = get_hash(content)

    if url in page_history:

        if page_history[url] == new_hash:
            print(f"{url}")
            print("No changes detected. Skipping crawl.")
            return

        print(f"{url}")
        print("Changes detected. Re-crawling page.")

    else:
        print(f"{url}")
        print("New page discovered. Crawling.")

    page_history[url] = new_hash


# First crawl
crawl_page(
    "https://quotes.toscrape.com/",
    "Distributed scraping with Celery workers"
)

# Same page, same content
crawl_page(
    "https://quotes.toscrape.com/",
    "Distributed scraping with Celery workers"
)

# Same page, changed content
crawl_page(
    "https://quotes.toscrape.com/",
    "Distributed scraping with Celery workers and Redis"
)