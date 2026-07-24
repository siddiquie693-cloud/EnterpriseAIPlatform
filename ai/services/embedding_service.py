

class EmbeddingService:
    """
    Service for generating text embeddings using sentenceTransformer.
    """

    _model = None

    def __init__(self):
        if EmbeddingService._model is None:
            EmbeddingService._model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2",
                local_files_only=False,
            )

        self.model = EmbeddingService._model

    def generate_embedding(self, text):
        return self.model.encode(text)

    def generate_embeddings(self, texts):
        """
        generate embeddings for a list of texts.
        """
        return self.model.encode(texts)    