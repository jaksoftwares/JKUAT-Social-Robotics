# models.py
from django.db import models

class ExampleModel(models.Model):
    # Example fields
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
