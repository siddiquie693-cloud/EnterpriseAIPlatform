class ChunkingService:
    """
    Service for splitting large documents into smaller chunks.
    """

    @staticmethod
    def split_text(text: str, chunk_size: int = 1000, overlap: int = 200):
        """
        split text into overlapping chunks.

        Agrs:
        text: Input document text
        chunk_size: Number of characters per chunk
        overlap: Overlapping characters between chunks

        Returns:
        List[str]
        """
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks
        