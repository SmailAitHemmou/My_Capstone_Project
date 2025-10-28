from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        return Movie.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
