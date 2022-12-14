from django.db import models
from user.models import User 
from category.models import Category


class Todo(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    description = models.TextField(blank=True, default="")
    category = models.ManyToManyField(Category, related_name="categories", blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
