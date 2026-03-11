from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()


def search_web(query: str):
    results = tavily.search(query=query, max_results=5)

    urls = []
    for r in results["results"]:
        urls.append(r["url"])

    return urls