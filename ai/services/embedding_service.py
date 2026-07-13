from sentence_transformers import SentenceTransformer
class EmbeddingService:
    """
    Service for generating text embeddings using sentenceTransformer.
    """
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def generate_embedding(self, text: str):
        """
        Generate embeddings for a single text.
        """
        return self.model.encode(text)

    def generate_embeddings(self, texts):
        """
        generate embeddings for a list of texts.
        """
        return self.model.encode(texts)    