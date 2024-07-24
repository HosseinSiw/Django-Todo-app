from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'users'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page="home:home"), name='logout'),
]
