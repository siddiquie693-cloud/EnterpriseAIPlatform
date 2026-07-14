from pypdf import PdfReader
import os

class DocumentService:
    """
    Handles document processing.
    """

    @staticmethod
    def extract_text(file_path: str) -> str:
        print(f"Reading file: {file_path}")
        print(f"Exists: {os.path.exists(file_path)}")
        print(f"Size: {os.path.getsize(file_path)} bytes")
        
        reader = PdfReader(file_path)

        text = ""
        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()        