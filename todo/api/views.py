from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from rest_framework import status

from ..models import Todo 
from .serializers import TodoSerializer
from .permissions import IsOwner


class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset
    
    def get(self, request):
        queryset = self.get_queryset()
        context = {
            "request": request
        }
        serializer = TodoSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def post(self, request):
        context = {
            "request": request
        }
        serializer = TodoSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.validated_data["user"] = request.user 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "slug"
    permission_classes = [IsOwner]
