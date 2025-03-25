from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_works, name='home'),  # 👈 This maps root '/' to the insert view
    path('insert/', views.insert_works, name='insert_works'),
    path('search/', views.search_employees, name='search_employees'),
]
