from venv import create
from django.db import models

# Create your models here.
class AppModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name