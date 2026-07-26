# Distributed RAG Scraper Framework

## Author

Noura S. Al Hassanieh

## Course Project
The Distributed RAG Scraper Framework is a web data collection and question-answering system that combines distributed web scraping, vector search, and Retrieval-Augmented Generation (RAG).

The framework collects information from websites using Scrapy and Playwright, processes and stores the extracted content in a vector database (Qdrant), and answers user questions through a FastAPI backend using semantic retrieval and a FLAN-T5 language model.

## The system supports:

Static website scraping
JavaScript-rendered website scraping
Distributed task processing
Semantic vector search
Retrieval-Augmented Generation (RAG)
Source attribution and citations
System Architecture

## The system consists of the following components:

FastAPI Backend
Scrapy Crawlers
Playwright Browser Automation
Redis Queue
Celery Workers
PostgreSQL Database
Qdrant Vector Database
SentenceTransformer Embedding Model
FLAN-T5 Language Model
Architecture Diagram

## Architecture Diagram

The system architecture is provided in:

- diagrams/Architecture Diagram.pdf


# Workflow

The framework follows the workflow below:

Crawl websites using Scrapy and Playwright.
Extract content from webpages.
Generate embeddings using SentenceTransformer.
Store embeddings in Qdrant.
Receive user questions through FastAPI.
Generate query embeddings.
Retrieve relevant documents from Qdrant.
Generate answers using FLAN-T5.
Return the answer together with supporting sources.

## Flowchart

See:
diagrams/Flowchart.pdf
Features
Web Scraping
Static Website Scraping

The framework successfully scrapes content from:
https://quotes.toscrape.com/

## Data extracted includes:

Quote text
Author name
Tags
JavaScript-Rendered Website Scraping

Playwright is used to scrape dynamically rendered content from:
https://quotes.toscrape.com/js/


This demonstrates support for modern JavaScript-heavy websites.

Pagination Crawling

The crawler automatically follows paginated links.

Results achieved:

10 pages crawled
100 items collected

Responsible Crawling

The framework implements ethical scraping practices.

Robots.txt Compliance

ROBOTSTXT_OBEY = True
Show more lines
Rate Limiting

DOWNLOAD_DELAY = 1
Show more lines
Per-Domain Request Limiting

CONCURRENT_REQUESTS_PER_DOMAIN = 1
Show more lines
AutoThrottle

AUTOTHROTTLE_ENABLED = True


These settings reduce server load and improve crawling behavior.

Distributed Processing
Redis

Redis is used as a message broker to manage scraping tasks.

Responsibilities:

Queue management
Task distribution
Worker communication
Celery

Celery workers execute scraping tasks asynchronously.

Benefits:

Parallel execution
Scalability
Improved performance
Distributed processing
Data Storage
PostgreSQL

PostgreSQL stores metadata related to scraping operations and collected documents.

Examples include:

URLs
Crawl status
Document information
Qdrant Vector Database

Qdrant stores vector embeddings generated from document content.

Configuration:


Vector Size = 384
Distance = COSINE


Capabilities:

Semantic search
Similarity matching
Fast vector retrieval
Retrieval-Augmented Generation (RAG)
Embedding Generation

## The framework uses:

all-MiniLM-L6-v2

through SentenceTransformer to convert text into vector embeddings.

Semantic Retrieval

User questions are converted into embeddings and matched against stored vectors using Qdrant.

Example:

Query: distributed workers


Retrieved result:

Distributed scraping with Celery workers
Answer Generation

## The framework uses:
google/flan-t5-base

to generate answers using retrieved context.

RAG Endpoint

Example request:

GET /rag?question=How does the system scale?

Example response:

{
"answer": "Distributed scraping with Celery workers",
"sources": [
"Distributed scraping with Celery workers"
]
}

This demonstrates retrieval combined with generation and source attribution.

API Endpoints
Health Check
Request
GET /
Response
JSON

{
"status": "running"
}
Semantic Search
Request
GET /search

Example
HTTP
/search?query=distributed workers

Response
JSON
[
{
"text": "Distributed scraping with Celery workers"
}
]
RAG Question Answering
Request
HTTP
GET /rag

Example
HTTP
/rag?question=How does the system scale?
Response
JSON
{
"answer": "Distributed scraping with Celery workers",
"sources": [
"Distributed scraping with Celery workers"
]}


## Technologies Used
Python
FastAPI
Scrapy
Playwright
Redis
Celery
PostgreSQL
Qdrant
SentenceTransformer
FLAN-T5
Docker


## Project Structure
backend/
├── api/
├── rag/
│
scraper/
│
workers/
│
database/
│
diagrams/
├── Architecture Diagram.drawio
├── Architecture Diagram.pdf
├── Flowchart.drawio
└── Flowchart.pdf

README.md
docker-compose.yml

## Running the Project
Start Infrastructure
Shell

docker compose up -d

Run FastAPI
Shell

uvicorn backend.api.main:app --reload

Open Swagger

http://127.0.0.1:8000/docs

Results

## The framework successfully demonstrated:

Static website scraping
JavaScript-rendered website scraping
Pagination crawling
Distributed task execution
Vector storage using Qdrant
Semantic search
Retrieval-Augmented Generation
Source attribution
FastAPI-based API access
Future Improvements
Additional website support
Improved answer quality through larger language models
Complete Docker backend containerization
Authentication and user management
Advanced monitoring and analytics