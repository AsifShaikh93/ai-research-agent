from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from langchain_classic.prompts import PromptTemplate
from app.rag import add_documents, retrieve_documents
from app.tools import search_web
from app.scraper import scrape_url
from app.models import AgentState
import os

groq_api_key = os.getenv("GROQ_API_KEY")


if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)


def search_node(state: AgentState):

    urls = search_web(state["query"])

    return {"urls": urls}


def scrape_node(state: AgentState):

    docs = []

    for url in state["urls"]:
        docs.append(scrape_url(url))

    return {"documents": docs}


def store_node(state: AgentState):

    add_documents(state["documents"])

    return {"documents": state["documents"]}

def retrieve_node(state: AgentState):

    context = retrieve_documents(state["query"])

    return {"context": context}


def summarize_node(state: AgentState):

    prompt = PromptTemplate(
        template="""
You are a research assistant.

Use the following context to answer the research question.

Context:
{context}

Question:
{question}

Write a detailed report with key insights.
""",
        input_variables=["context", "question"]
    )

    chain = prompt | llm

    result = chain.invoke({
        "context": state["context"],
        "question": state["query"]
    })

    return {"report": result.content}


workflow = StateGraph(AgentState)

workflow.add_node("search", search_node)
workflow.add_node("scrape", scrape_node)
workflow.add_node("store", store_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("summarize", summarize_node)

workflow.set_entry_point("search")

workflow.add_edge("search", "scrape")
workflow.add_edge("scrape", "store")
workflow.add_edge("store", "retrieve")
workflow.add_edge("retrieve", "summarize")
workflow.add_edge("summarize", END)

research_agent = workflow.compile()