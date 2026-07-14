from ai.services.document_service import DocumentService
from ai.services.chunking_service import ChunkingService
from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService

class DocumentIndexService:
    """
    Handles omplete document indexing pipeline.
    """
    def __init__(self):
        self.document_service = DocumentService()
        self.chunking_service = ChunkingService()
        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

    def index_document(self, document):
         
        """
         Extract text, generate chunks,
        create embeddings, update FAISS index.
        """

        # Extract text from PDF 
        text = self.document_service.extract_text(document.file.path)

        # Split into chunks 
        chunks = self.chunking_service.chunk_text(text)

        if not chunks:

            return 

        # Generate embeddings 
        embeddings = self.embedding_service.generate_embeddings(chunks)

        # Load existing FAISS index 
        self.vector_service.load_index()

        # Add new document embeddings 
        self.vector_service.add_embeddings(embeddings, chunks,)

        # save updated FAISS index 
        self.vector_service.save_index() 
        
    