from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name_movie = models.CharField(max_length=200)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_movie
    
    class Meta:
        ordering = ['complete']
    


