from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService
from ai.services.llm_service import LLMService
from ai.models import Conversation

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

    def answer_question(self, question, document_id=None, conversation_id=None, top_k=3):
        """
        Answer a question using retrieved document context
        and previous conversation history.
        """

        # Load saved FAISS index
        self.vector_service.load_index()

        query_embedding = self.embedding_service.generate_embedding(question)

        search_results = self.vector_service.search(query_embedding, top_k=top_k, document_id=document_id,)

        context = "\n\n".join(
            chunk["text"] for chunk in search_results

        )

        history = []

        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id)

                for message in conversation.messages.all():
                    history.append(
                        {
                            "role": message.role,
                            "content": message.content,
                        }
                    )
            except Conversation.DoesNotExist:
                pass        

        answer = self.llm_service.answer_question(
            document=context,
            question=question,
            history=history,
        )

        return {
            "question": question,
            "context": search_results,
            "sources": list(
                {
                    chunk["document_id"]
                    for chunk in search_results
                }
            ),
            "citations": search_results,
            "answer": answer,
        }