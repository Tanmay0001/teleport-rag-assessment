import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add_documents(self, docs, embeddings):

        faiss.normalize_L2(embeddings)

        self.index.add(embeddings)
        self.documents.extend(docs)

    def search(self, query_embedding, top_k=3):

        query_embedding = np.array(
            [query_embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for rank, idx in enumerate(indices[0]):

            results.append({
                "rank": rank + 1,
                "score": float(scores[0][rank]),
                "document": self.documents[idx]
            })

        return results