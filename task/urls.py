from task.views import *
from django.urls import path

app_name='tasklist'

urlpatterns=[
    path('tasks/',tasks,name='tasks'),
]

