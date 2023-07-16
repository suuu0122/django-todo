from django.urls import path

from . import views



app_name = "todo_app"
urlpatterns = [
    path('', views.TodoList.as_view(), name="list"),
]