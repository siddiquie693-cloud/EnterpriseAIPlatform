from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService
from ai.services.llm_service import LLMService

class RAGService:
    """
    Retrieval-Augmented Generation (RAG) service.
    Retrieves relevant document chunks and sends them to the LLM.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()
        self.llm_service = LLMService()

    def load_document(self, chunks):
        """
        generate embeddings and store them in FAISS.
        """

        embeddings = self.embedding_service.generate_embeddings(chunks)
        self.vector_service.add_embeddings(embeddings, chunks)

    def answer_question(self, question, top_k=3):
        """
        Answer a question using retrieved document context.
        """

        # Load saved FAISS index
        self.vector_service.load_index()

        query_embedding = self.embedding_service.generate_embedding(question)

        context_chunks = self.vector_service.search(query_embedding, top_k=top_k)

        context = "\n\n".join(context_chunks)

        answer = self.llm_service.answer_question(
            document=context,
            question=question,
        )

        return {
            "question": question,
            "context": context_chunks,
            "answer": answer,
        }