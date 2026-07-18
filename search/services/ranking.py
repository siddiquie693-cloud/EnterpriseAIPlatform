class RankingService:
    """
    Merge BM25 and FAISS search results into one ranked list.
    """

    def merge_results(
            self,
            semantic_results,
            keyword_results,
            semantic_weight=0.7,
            keyword_weight=0.3,
    ):
        merged = {}

        # Add semantic results 
        for result in semantic_results:
            key = (
                result["document_id"],
                result["text"],
            )

            merged[key] = {
                **result,
                "semantic_score": result["score"],
                "keyword_score": 0.0,
            }

        # Merge keyword results 
        for result in keyword_results:
            key = (
                result["document_id"],
                result["text"],
            )

            if key in merged:

                merged[key]["keyword_score"] = result["bm25_score"]

            else:
                merged[key] = {
                    "document_id": result["document_id"],
                    "text": result["text"],
                    "semantic_score": 0.0,
                    "keyword_score": result["bm25_score"],
                }

        # Normalize BM25 scores 
        max_keyword = max(
            (
                item["keyword_score"]
                for item in merged.values()
            ),
            default=1,
        )

        for item in merged.values():
            keyword = item["keyword_score"] / max_keyword

            semantic = item["semantic_score"]

            item["final_score"] = round(
                semantic_weight * semantic
                + keyword_weight * keyword,
                4,
            )
        ranked = sorted(
            merged.values(),
            key=lambda x: x["final_score"],
            reverse=True,
        )

        return ranked                     
