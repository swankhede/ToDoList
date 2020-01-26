from django.db import models

# Create your models here.
class NoteSave(models.Model):
    Note = models.CharField(max_length=200)
    time =models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.Note
