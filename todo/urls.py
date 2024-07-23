from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path("my_todos/", views.TodoListView.as_view(), name="my_todos"),
    path("todo_details/<int:pk>/", views.TodoDetailView.as_view(), name="todo_details"),
    path("<int:pk>/update/", views.TodoUpdateView.as_view(), name="todo_update"),
    path("create/", views.TodoCreateView.as_view(), name="todo_create"),
]
