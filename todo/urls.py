from django.urls import path, include
from todo.api.views import TodoListCreateView, TodoDetailUpdateDestroyView


urlpatterns = [
    path("api/todos/", TodoListCreateView.as_view(), name="todo_list"),
    path("api/todos/<slug:slug>/", TodoDetailUpdateDestroyView.as_view(), name="todo_detail"),
    path("api/auth/", include("rest_framework.urls")),
]
