from django.urls import path

from fruits.views import *

app_name="karma"

urlpatterns=[
    path('apple/',apple,name='apple'),
    path('graphs/',graphs,name='graphs'),
]