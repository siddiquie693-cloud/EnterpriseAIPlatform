from django.core.management.base import BaseCommand

from documents.models import Document
from ai.services.document_index_service import DocumentIndexService
from ai.services.vector_service import VectorService

class Command(BaseCommand):
    help = "Rebuild the FAISS vector index from all documents."

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Rebuilding vector index..."))

        # Reset vector store 
        vector_service = VectorService()
        vector_service.index.reset()
        vector_service.chunks = []

        index_service = DocumentIndexService()

        documents = Document.objects.all()

        if not documents.exists():
            self.stdout.write(
                self.style.WARNING("No document found.")
            )
            return 
        for document in documents:
            try:
                self.stdout.write(f"Indexing: {document.id} - {document.title}")
                index_service.index_document(document)
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed to index document {document.id} ({document.title}): {e}"
                    )
                )

        # Save rebuit index 
        vector_service.index = index_service.vector_service.index
        vector_service.chunks = index_service.vector_service.chunks
        vector_service.save_index()

        self.stdout.write(
            self.style.SUCCESS(
                "Vector index rebuilt successfully!"
            )
        )            

