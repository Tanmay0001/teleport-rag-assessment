from sentence_transformers import SentenceTransformer
import numpy as np


class Embedder:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, texts):
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )
        return np.array(embeddings, dtype=np.float32)

    def embed_one(self, text):
        return self.embed([text])[0]