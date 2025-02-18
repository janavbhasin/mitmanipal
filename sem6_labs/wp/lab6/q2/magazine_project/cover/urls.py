from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover_form, name='cover_form'),
]
