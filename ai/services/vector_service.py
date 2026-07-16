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

    def add_embeddings(self, embeddings, chunks, document_id=None):
        """
        Add embeddings and corresponding text chunks.
        """

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        for chunk in chunks:
            self.chunks.append({"document_id": document_id, "text": chunk,})

    def search(self, query_embedding, top_k=3, document_id=None):
        """
        Return top-k most similar chunks.
        """
        

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, max(top_k * 5, top_k),)

        
        results = []

        for idx in indices[0]:
            if idx == -1:
                continue

            if idx >= len(self.chunks):
            
                continue


            chunk = self.chunks[idx]

            # Filter by document only if requested 

            
            if (document_id is not None and chunk["document_id"] != document_id):
                
                continue
            

            results.append(
                {
                    "document_id": chunk["document_id"],
                    "text": chunk["text"],
                }
            )

            if len(results) >= top_k:
                break

        

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
                 