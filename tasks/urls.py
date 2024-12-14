from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('detail/<int:task_id>/', views.task_detail, name='detail'),
]