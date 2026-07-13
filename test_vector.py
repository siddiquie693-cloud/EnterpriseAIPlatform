from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService

def main():
    chunks = [
        "Python is a programming language.",
        "Django is a python web framework",
        "FAISS is used for vector similarity search",
        "groq provides fast llm inference",
        "sentence transformers generate embeddings"
    ]

    print("loading embedding model....")
    embedding_service = EmbeddingService()

    print("generating embeddings...")
    embeddings = embedding_service.generate_embeddings(chunks)

    print(f"Generate {len(embeddings)} embeddings.")

    vector_service = VectorService()

    print("Adding embeddings to faiss...")
    vector_service.add_embeddings(embeddings, chunks)

    query = "What is django?"

    print(f"\nQuery: {query}")

    query_embedding = embedding_service.generate_embedding(query)

    results = vector_service.search(query_embedding, top_k=3)

    print("\nTop Results:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result}")

if __name__ == "__main__":
    main()        

