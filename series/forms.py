from django import forms
from .models import Serie

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'

