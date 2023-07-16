from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Todo



class TodoList(ListView):
    template_name = "todo_app/list.html"
    model         = Todo