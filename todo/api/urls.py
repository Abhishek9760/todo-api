from django.urls import path, include
from .views import (TodoListView, TodoDetailView)

app_name = "status"

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]

