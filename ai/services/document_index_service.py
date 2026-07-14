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

   # def index_document(self, document):
        
        # Extract text, generate chunks,
       # create embeddings, update FAISS index.
       # """

        # Extract text from PDF 
       # text = self.document_service.extract_text(document.file.path)

        # Split into chunks 
       # chunks = self.chunking_service.chunk_text(text)

       # if not chunks:
        #    return 

        # Generate embeddings 
        #embeddings = self.embedding_service.generate_embeddings(chunks)

        # Load existing FAISS index 
        #self.vector_service.load_index()

        # Add new document embeddings 
       # self.vector_service.add_embeddings(embeddings, chunks,)

        # save updated FAISS index 
        #self.vector_service.save_index() 
        
    def index_document(self, document):
        print("\n========== DOCUMENT INDEXING STARTED ==========")

        print("Step 1: Extracting text...")
        text = self.document_service.extract_text(document.file.path)
        print(f"Extracted {len(text)} characters")

        print("Step 2: Chunking...")
        chunks = self.chunking_service.chunk_text(text)
        print(f"Created {len(chunks)} chunks")

        if not chunks:
            print("No chunks created.")
            return

        print("Step 3: Generating embeddings...")
        embeddings = self.embedding_service.generate_embeddings(chunks)
        print(f"Generated {len(embeddings)} embeddings")

        print("Step 4: Loading FAISS index...")
        self.vector_service.load_index()

        print("Step 5: Adding embeddings...")
        self.vector_service.add_embeddings(embeddings, chunks)

        print("Step 6: Saving FAISS index...")
        self.vector_service.save_index()

        
        print("========== DOCUMENT INDEXING COMPLETED ==========\n")   