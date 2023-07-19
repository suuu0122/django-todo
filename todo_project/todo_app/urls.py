from django.urls import path

from . import views



app_name = "todo_app"
urlpatterns = [
    path('list/', views.TodoList.as_view(), name="list"),
    path('detail/<int:pk>', views.TodoDetail.as_view(), name="detail"),
    path('create/', views.TodoCreate.as_view(), name="create"),
]