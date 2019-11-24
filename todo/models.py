from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo")
    todo = models.CharField(max_length=500)

    def __str__(self):
        return self.todo
