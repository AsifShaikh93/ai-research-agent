from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import os



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="research_docs",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

# create vector store properly
vectorstore = QdrantVectorStore(
    client=client,
    collection_name="research_docs",
    embedding=embeddings # Note: 'embedding' (singular) in this class
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

def add_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    clean_docs = [d for d in docs if d and len(d.strip()) > 20]

    if clean_docs:
        chunks = text_splitter.create_documents(clean_docs)
        vectorstore.add_documents(chunks)


def retrieve_documents(query):

    results = vectorstore.similarity_search(query, k=4)

    texts = [r.page_content for r in results]

    return "\n".join(texts)