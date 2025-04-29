from django.db import models

# Create your models here.
class ToDo(models.Model):
    content = models.TextField(null=False, max_length=255)