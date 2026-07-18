from rank_bm25 import BM25Okapi

class BM25Service:
    """
    Keyword-based search using BM25.
    """

    def __init__(self):
        self.documents = []
        self.metadata = []
        self.bm25 = None

    def build_index(self, chunks):
        """
        build BM25 index from document chunks.

        chunks format:
        [
            {
                "document_id": 1,
                "text": "Artificial Intelligence ..."
            }
        ]
        """

        self.documents = []
        self.metadata = []

        tokenized = []

        for chunk in chunks:
            text = chunk["text"]

            self.documents.append(text)
            self.metadata.append(chunk)

            tokenized.append(text.lower().split())

        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, top_k=5, document_id=None):
        """
        Keyword search.
        """
        if self.bm25 is None:
            return []

        scores = self.bm25.get_scores(
            query.lower().split()
        )

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True,
        )

        results = []
        seen = set()

        for idx, score in ranked:
            chunk = self.metadata[idx]

            if (
                document_id is not None
                and chunk["document_id"] != document_id
            ):
                continue

            # Remove duplicates 
            if chunk["text"] in seen:
                continue

            seen.add(chunk["text"])
            
            results.append(
                {
                    "document_id": chunk["document_id"],
                    "text": chunk["text"],
                    "bm25_score": float(score),
                }
            )

            if len(results) >= top_k:
                break

        return results    

        