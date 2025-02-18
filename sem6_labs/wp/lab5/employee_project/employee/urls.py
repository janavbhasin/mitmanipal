from django.urls import path
from . import views

urlpatterns = [
    path('promotion/', views.promotion_eligibility, name='promotion_eligibility'),
]
