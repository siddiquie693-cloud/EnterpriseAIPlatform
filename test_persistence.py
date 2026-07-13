from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService


def main():
    chunks = [
        "Python is a programming language.",
        "Django is a Python web framework.",
        "FAISS performs similarity search.",
        "Groq provides fast LLM inference.",
        "Sentence Transformers generate embeddings."
    ]

    embedding_service = EmbeddingService()

    print("Generating embeddings...")
    embeddings = embedding_service.generate_embeddings(chunks)

    print("Creating vector index...")
    vector_service = VectorService()

    vector_service.add_embeddings(embeddings, chunks)

    print("Saving index...")
    vector_service.save_index()

    print("\nCreating a new VectorService instance...")

    new_vector_service = VectorService()

    print("Loading saved index...")
    new_vector_service.load_index()

    query = "What is Django?"

    query_embedding = embedding_service.generate_embedding(query)

    results = new_vector_service.search(query_embedding)

    print("\nTop Results:")

    for i, result in enumerate(results, start=1):
        print(f"{i}. {result}")


if __name__ == "__main__":
    main()