from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['TAVILY_API_KEY']=os.getenv('TAVILY_API_KEY')

tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def search_web(query: str):
    results = tavily.search(query=query, max_results=5)

    urls = []

    for r in results["results"]:
        urls.append(r["url"])

    return urls