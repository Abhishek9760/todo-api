from django.urls import path, include
from .views import (TodoListView, TodoDetailView)

app_name = "status"

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    # path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]

