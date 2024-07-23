# from django.shortcuts import render
from django.views.generic import TemplateView
from todo.models import Todo


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()  # Must be edited
        return context
