from django.urls import path
from cal.views import *

app_name='calculater'

urlpatterns=[
    path('calc/',calc,name='calc'),
    path('gopal/',gopal,name='gopal')
]