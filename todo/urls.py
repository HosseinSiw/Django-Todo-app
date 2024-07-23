from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path("my_todos/", views.TodoListView.as_view(), name="my_todos"),
]
