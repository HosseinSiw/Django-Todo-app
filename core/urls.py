from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include('users.urls')),
    path("", include('home.urls'), name="home"),
    path('todo/', include("todo.urls"), name="todo"),
]
