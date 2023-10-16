from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='Task List'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='Task Detail')
]
