from django.db import models
from user.models import User 


class Todo(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    description = models.TextField(blank=True, default="")
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
