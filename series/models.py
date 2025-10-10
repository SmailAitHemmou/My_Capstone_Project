from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Serie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name_serie = models.CharField(max_length=200)
    episodes_total = models.PositiveIntegerField(help_text="Total number of episodes in the serie")
    episodes_watched = models.PositiveIntegerField(default=0, help_text="Number of episodes watched")
    release_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.episodes_total < 0 or self.episodes_watched < 0:
            raise ValidationError("Episode numbers cannot be negative.")
        
        if self.episodes_watched > self.episodes_total:
            raise ValidationError("Watched episodes cannot exceed the total number of episodes.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name_serie} ({self.episodes_watched}/{self.episodes_total})"


    class Meta:
        ordering = ['complete']  
