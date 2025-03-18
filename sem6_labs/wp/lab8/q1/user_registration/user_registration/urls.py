# user_registration/urls.py
from django.contrib import admin
from django.urls import path
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('success/', views.success, name='success'),
]
