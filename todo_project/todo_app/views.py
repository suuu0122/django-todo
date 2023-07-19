from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Todo



class TodoList(ListView):
    template_name = "todo_app/list.html"
    model         = Todo



class TodoDetail(DetailView):
    template_name = "todo_app/detail.html"
    model         = Todo