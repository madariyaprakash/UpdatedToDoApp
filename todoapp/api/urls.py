
from django.urls import path
from api.views import (
    ListTasks,
    DetailTask,
    UpdateTask,
    CreateTask,
    DeleteTask,

)


urlpatterns = [
    path('task-list/', ListTasks.as_view(), name='task-list'),
    path('task-detail/<str:pk>/', DetailTask.as_view(), name='task-detail'),
    path('task-update/<str:pk>/', UpdateTask.as_view(), name='task-update'),
    path('task-create/', CreateTask.as_view(), name='task-create'),
    path('task-delete/<str:pk>/', DeleteTask.as_view(), name='task-delete'),
]