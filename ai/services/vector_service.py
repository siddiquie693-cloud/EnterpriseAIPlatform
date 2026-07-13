import os
import pickle

import faiss
import numpy as np

class VectorService:
    """
    Service for creating, saving, loading, and searching a FAISS vector index.
    """

    INDEX_FILE = "vector_store/index.faiss"
    CHUNKS_FILE = "vector_store/chunks.pkl"

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
    
    def save_index(self):
        """
        Save FAISS index and chunks to disk.
        """
        os.makedirs("vector_store", exist_ok=True)

        faiss.write_index(self.index, self.INDEX_FILE)

        with open(self.CHUNKS_FILE, "wb") as file:
            pickle.dump(self.chunks, file)

    def load_index(self):
        """
        Load FAISS index and chunks from disk.
        """
        if os.path.exists(self.INDEX_FILE):
            self.index = faiss.read_index(self.INDEX_FILE)

        if os.path.exists(self.CHUNKS_FILE):
            with open(self.CHUNKS_FILE, "rb") as file:
                self.chunks = pickle.load(file)            
                 