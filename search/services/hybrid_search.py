from ai.services.embedding_service import EmbeddingService
from ai.services.vector_service import VectorService

from search.services.bm25_service import BM25Service
from search.services.ranking import RankingService

class HybridSearchService:
    """
    Hybrid Search using:
    1. FAISS Semantic Search
    2. BM25 Keyword Search
    3. Hybrid Ranking
    """

    #def __init__(self):
        #self.embedding_service = EmbeddingService()

        ##self.vector_service = VectorService()
        #self.vector_service.load_index()

        #self.bm25_service = BM25Service()

        # Build BM25 index using existing vector chunks 
        #self.bm25_service.build_index(
            #self.vector_service.chunks
        #)

        #self.ranking_service = RankingService()

    def search(self, query, top_k=5, document_id=None,):
        """
        Perform Hybrid Search.
        """

        # Lazy initialization
        embedding_service = EmbeddingService()
        vector_service = VectorService()
        vector_service.load_index()

        bm25_service = BM25Service()
        bm25_service.build_index(vector_service.chunks)

        ranking_service = RankingService()

        query_embedding = self.embedding_service.generate_embedding(query)

        semantic_results = vector_service.search(
            query_embedding=query_embedding,
            top_k=top_k,
            document_id=document_id,
        )

        keyword_results = self.bm25_service.search(
            query=query,
            top_k=top_k,
            document_id=document_id,
        )

        final_results = ranking_service.merge_results(
            semantic_results,
            keyword_results,
        )

        return {
            "results": final_results,
        }
    