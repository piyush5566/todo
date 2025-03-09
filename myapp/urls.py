from django.urls import path
from .views import hello_django, get_all_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('hello/', hello_django, name='hello_django'),
    path('', get_all_tasks, name='get_all_tasks'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/update/<int:task_id>/', update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
]
