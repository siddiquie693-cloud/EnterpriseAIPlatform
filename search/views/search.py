from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from search.services.hybrid_search import HybridSearchService
from search.serializers import SearchSerializer

from drf_spectacular.utils import extend_schema
@extend_schema(
    request=SearchSerializer,
    responses={200: dict},
)

class HybridSearchAPIView(APIView):
    """
    Hybrid Search API
    (Semantic + Keyword + Hybrid Ranking)
    """

    permission_classes = [IsAuthenticated]

    serializer_class = SearchSerializer

    def post(self, request):
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = HybridSearchService()

        results = service.search(
            query=serializer.validated_data["query"],
            document_id=serializer.validated_data.get("document_id"),
            top_k=serializer.validated_data.get("top_k", 5),
        )

        return Response(
            {
                "status": "success",
                "query": serializer.validated_data["query"],
                "count": len(results["results"]),
                "results": results["results"],
            },

            status=status.HTTP_200_OK,
        )

        