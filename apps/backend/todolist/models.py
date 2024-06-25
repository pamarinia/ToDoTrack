from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
