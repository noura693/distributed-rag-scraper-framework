import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod h3 a")

print("Books Found:")

for book in books[:5]:
    print(book["title"])