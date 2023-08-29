from django.db import models

# Create your models here.

# ORM: object relational schema used for databases

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)