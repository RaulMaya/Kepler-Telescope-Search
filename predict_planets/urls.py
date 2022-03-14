from django.urls import path
from . import views

urlpatterns = [
    #HomePage
    path('', views.index)
]