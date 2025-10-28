from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = [
            'id',
            'user',
            'name_serie',
            'episodes_total',
            'episodes_watched',
            'release_year',
            'description',
            'complete',
            'created'
        ]
