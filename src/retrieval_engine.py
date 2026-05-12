from src.dataset import TECHNICAL_CORPUS
from src.embedder import Embedder
from src.vector_store import VectorStore
from src.mocks.vertexai_mock import GenerativeModel


class RetrievalEngine:

    def __init__(self):

        self.embedder = Embedder()

        self.vector_store = VectorStore(
            dimension=384
        )

        self.generative_model = GenerativeModel()

        self.ingest_documents()

    def ingest_documents(self):

        texts = [
            doc["text"]
            for doc in TECHNICAL_CORPUS
        ]

        embeddings = self.embedder.embed(texts)

        self.vector_store.add_documents(
            TECHNICAL_CORPUS,
            embeddings
        )

    def strategy_a(self, query):

        query_embedding = self.embedder.embed_one(query)

        return self.vector_store.search(
            query_embedding,
            top_k=3
        )

    def expand_query(self, query):

        prompt = f"""
Expand this query for better semantic retrieval:

{query}
"""

        response = self.generative_model.generate_content(prompt)

        return response.text

    def strategy_b(self, query):

        expanded_query = self.expand_query(query)

        query_embedding = self.embedder.embed_one(expanded_query)

        results = self.vector_store.search(
            query_embedding,
            top_k=3
        )

        return {
            "expanded_query": expanded_query,
            "results": results
        }