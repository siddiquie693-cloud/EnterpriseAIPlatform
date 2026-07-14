from pypdf import PdfReader
from pypdf.errors import PdfReadError, PdfStreamError

class DocumentService:
    """
    Handles document processing.
    """

    @staticmethod
    def extract_text(file_path: str) -> str:
        try:
            reader = PdfReader(file_path)

            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

            return text.strip()
        except (PdfReadError, PdfStreamError):
            raise ValueError("Invalid or corrupted PDF file.")      