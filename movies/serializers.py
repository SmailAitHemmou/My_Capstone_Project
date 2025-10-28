from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'user', 'name_movie', 'release_year', 'description', 'complete', 'created']
