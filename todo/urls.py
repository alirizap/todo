from django.urls import path, include
from todo.api import views


urlpatterns = [
    path("api/todos/", views.TodoListCreateView.as_view(), name="todo_list"),
    path("api/todos/<slug:slug>/", views.TodoDetailUpdateDestroyView.as_view(), name="todo_detail"),
    path("api/auth/", include("rest_framework.urls")),
    path("api/register/", views.UserCreate.as_view(), name="register")
]
