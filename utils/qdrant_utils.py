from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION")

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def setup_collection():
    collections = client.get_collections().collections
    if not any(c.name == COLLECTION_NAME for c in collections):
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=192, distance=Distance.COSINE)
        )

setup_collection()

def store_vector(vector, metadata):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload=metadata
            )
        ]
    )

def search_similar(vector, top_k=5):
    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=top_k,
        with_vectors=True
    )
    return [{"score": hit.score, "payload": hit.payload, "vector": hit.vector} for hit in hits]