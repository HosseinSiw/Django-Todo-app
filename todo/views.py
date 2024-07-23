from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from todo.models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo_details.html'

    # we can also override the get_context_data method

    # def get_context_data(self, *args,**kwargs):
    #     context = super(TodoDetailView, self).get_context_data(*args, **kwargs)
    #
    #     context['title'] = context['object'].title
    #     return context


class TodoUpdateView(UpdateView):
    model = Todo
    context_object_name = 'todo'
    fields = ['title', 'description']
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:my_todos')


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/todo_create.html"
    fields = ['title', 'description']
    context_object_name = 'todo'
    success_url = reverse_lazy('todo:my_todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todo:my_todos')
    template_name = 'todo/todo_delete_confirm.html'
