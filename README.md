# AI Research Agent

An autonomous AI agent that performs web research using:

- LangGraph
- RAG pipeline
- Tavily search
- FastAPI
- Qdrant vector store

## Features

- Autonomous research workflow
- Web search
- Document retrieval
- LLM summarization
- REST API
- Kubernetes deployable

## Run locally

pip install -r requirements.txt

uvicorn app.main:app --reload


## API

POST /research

{
 "query": "Future of AI agents"
}