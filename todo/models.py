from uuid import uuid4
from django.db import models
from user.models import User 
from category.models import Category


class Todo(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=75, null=True, blank=True)
    # uuid -> used by API to lookup todo record
    uuid = models.UUIDField(db_index=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    description = models.TextField(blank=True, default="")
    category = models.ManyToManyField(Category, related_name="categories", blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
