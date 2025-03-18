# vote_project/urls.py
from django.contrib import admin
from django.urls import path
from voting import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vote, name='vote'),
]
