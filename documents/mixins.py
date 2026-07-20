from documents.models import Document

class DocumentQuerysetMixin:
    """
    Provides a queryset based on the authenticated user's role.
    """
    include_inactive = False

    def get_queryset(self):
        # Fix for drf-dpectacular schema generation
        if getattr(self, "swagger_fake_view", False):
            return Document.objects.none()
        
        user = self.request.user

        queryset = Document.objects.all()

        if not self.include_inactive:
            queryset = queryset.filter(is_active=True)

        if user.groups.filter(name="Admin").exists():
            return queryset
        return queryset.filter(uploaded_by=user)    