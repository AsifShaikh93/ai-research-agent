from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import research_agent

app = FastAPI(title="AI Research Agent")


class QueryRequest(BaseModel):
    query: str


@app.post("/research")
def research(request: QueryRequest):

    result = research_agent.invoke({
        "query": request.query
    })

    return {
        "query": request.query,
        "report": result["report"]
    }