from django.urls import path
from food.views import *

app_name="enjoy"

urlpatterns=[
    path('chicken/',chicken,name='chicken'),
    path('biryani/',biryani,name="biryani"),
]