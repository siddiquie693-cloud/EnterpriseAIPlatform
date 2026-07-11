from rest_framework.permissions import IsAuthenticated

class IsDocumentUser(IsAuthenticated):
    """
    Only authenticated users can access document APIs.
    """
    pass