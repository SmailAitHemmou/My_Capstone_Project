from rest_framework import viewsets, permissions
from .models import Serie
from .serializers import SerieSerializer

class SerieViewSet(viewsets.ModelViewSet):
    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       
        return Serie.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
      
        serializer.save(user=self.request.user)
