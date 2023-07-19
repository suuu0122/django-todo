from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Todo



class TodoList(ListView):
    template_name = "todo_app/list.html"
    model         = Todo



class TodoDetail(DetailView):
    template_name = "todo_app/detail.html"
    model         = Todo



class TodoCreate(CreateView):
    template_name = "todo_app/create.html"
    model         = Todo
    fields        = ("title", "memo", "priority", "duedate")
    success_url   = reverse_lazy("todo_app:list")



class TodoDelete(DeleteView):
    template_name = "todo_app/delete.html"
    model         = Todo
    success_url   = reverse_lazy("todo_app:list")



class TodoUpdate(UpdateView):
    template_name = "todo_app/update.html"
    model         = Todo
    fields        = ("title", "memo", "priority", "duedate")
    success_url   = reverse_lazy("todo_app:list")