from django.views.generic import TemplateView
from todo.models import Todo


class HomeView(TemplateView):
    """
    A simple view for the home page
    """
    template_name = 'home/home.html'

