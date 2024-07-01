from django.urls import path
from . import views 

urlpatterns = [
    path('myapi', views.myapi,name ='myapi'),
]

