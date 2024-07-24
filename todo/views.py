from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from todo.models import Todo
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView
)


class TodoListView(ListView, LoginRequiredMixin):
    """
    This class will represent the todo's list view
    """
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailView(DetailView, LoginRequiredMixin):
    """
    This class will represent the detail page of a single-Todo-object.
    """
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo_details.html'

    # we can also override the get_context_data method

    # def get_context_data(self, *args,**kwargs):
    #     context = super(TodoDetailView, self).get_context_data(*args, **kwargs)
    #
    #     context['title'] = context['object'].title
    #     return context


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class-based view for updating and existing Todo item.

    This view handles the modification of an existing Todo object via a form submission.
    It ensures that only authenticated users can update their own Todos.
    """
    model = Todo
    context_object_name = 'todo'
    fields = ['title', 'description']
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:my_todos')


class TodoCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view for creating new Todo items.

    This view handles the creation of new Todo objects via a form submission.
    It ensures that only authenticated users can create new Todos.
    """
    model = Todo
    template_name = "todo/todo_create.html"
    fields = ['title', 'description']
    context_object_name = 'todo'
    success_url = reverse_lazy('todo:my_todos')

    def form_valid(self, form):
        """
        Hook method to save the form data and set the current user as the creator.

        Overrides the default form_valid method to assign the current user to the form instance.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoDeleteView(DeleteView):
    """
    Class-based view for deleting a Todo item.

    This view handles the deletion of a Todo object identified by its primary key.
    """
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todo:my_todos')
    template_name = 'todo/todo_delete_confirm.html'


class TodoDoneView(View):
    """
    Class-based view for marking a Todo item as completed.

    This view sets the 'done' attribute of a Todo object to True, indicating completion.
    """

    def get(self, request, pk, *args, **kwargs):
        """
        Handles GET requests to mark a Todo item as completed.

        Retrieves the Todo item by its primary key, marks it as done, and redirects to the todos list.
        """
        todo = Todo.objects.get(pk=pk)
        todo.done = True
        return redirect("todo:my_todos")