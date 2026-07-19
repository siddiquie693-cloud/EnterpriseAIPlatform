from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

@extend_schema(
    tags=["system"],
    summary="Health Check",
    description="Return the current health status of the Enterprise AI Platform.",
    responses={
        200: OpenApiResponse(
            description="Application is running successfully."
        )
    },
)

class HealthCheckAPIView(APIView):
    permission_classes = []
    
    def get(self, request):
        return Response(
            {
                "status": "success",
                "message": "Enterprise AI Knwoledge Platform is running",
            }
        )
