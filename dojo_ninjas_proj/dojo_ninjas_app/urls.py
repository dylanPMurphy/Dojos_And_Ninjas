from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('createDojo', views.createDojo),
    path('createNinja', views.createNinja)
]