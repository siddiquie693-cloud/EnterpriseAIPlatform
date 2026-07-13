import faiss
import numpy as np

class VectorService:
    """
    Service for creating and searching a FAISS vector index.
    """

    def __init__(self, dimension=384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add_embeddings(self, embeddings, chunks):
        """
        Add embeddings and corresponding text chunks.
        """

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        """
        Return top-k most similar chunks.
        """

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            if idx != -1:
                results.append(self.chunks[idx])
        return results
                 