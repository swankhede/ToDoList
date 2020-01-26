from .models import NoteSave
from django import forms
class save(forms.ModelForm):
    class Meta:
        model = NoteSave
        fields = '__all__'