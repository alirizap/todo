from rest_framework import serializers
from ..models import Todo 


class TodoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Todo 
        fields = ["title", "url", "user", "category", "description", "complete", "created_at", "updated_at"]
        read_only_fields = ("slug",)
        extra_kwargs = {
            'url': {'lookup_field': 'slug', 'view_name': 'todo_detail'}
        }