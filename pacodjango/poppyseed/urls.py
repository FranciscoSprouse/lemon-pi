from django.urls import path

from . import views

urlpatterns = [
    path('hydration/', views.hydration, name='hydration'),
]