import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from ai.services.rag_service import RAGService


def main():
    chunks = [
        "Python is a high-level programming language.",
        "Django is a powerful Python web framework used for backend development.",
        "FAISS is a library for efficient similarity search and clustering of dense vectors.",
        "Sentence Transformers generate semantic vector embeddings from text.",
        "Groq provides ultra-fast inference for Large Language Models."
    ]

    print("Initializing RAG Service...")
    rag_service = RAGService()

    print("Loading document into vector database...")
    rag_service.load_document(chunks)

    question = "What is Django?"

    print(f"\nQuestion: {question}")

    result = rag_service.ask(question)

    print("\nRetrieved Context:")
    for i, chunk in enumerate(result["context"], start=1):
        print(f"{i}. {chunk}")

    print("\nAI Answer:")
    print(result["answer"])


if __name__ == "__main__":
    main()