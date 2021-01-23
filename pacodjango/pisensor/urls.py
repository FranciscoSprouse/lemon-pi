from django.urls import path
from . import views

urlpatterns = [
    path('', views.hydration, name='hydration'),
]