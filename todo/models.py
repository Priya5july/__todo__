from django.db import models
from django.utils import timezone

# Create your models here.

class todo_data(models.Model):
    titel=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.titel
