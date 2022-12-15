from django.contrib.auth import get_user_model, password_validation
from django.core import exceptions
from rest_framework import serializers
from ..models import Todo 

User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Todo 
        fields = ["title", "url", "user", "category", "description", "complete", "created_at", "updated_at"]
        read_only_fields = ("slug", "user")
        extra_kwargs = {
            'url': {'lookup_field': 'slug', 'view_name': 'todo_detail'}
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get("password")
        try:
            password_validation.validate_password(password=password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(data)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user 

    class Meta:
        model = User 
        fields = ["username", "email", "password"]