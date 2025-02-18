from django.contrib import admin
from django.urls import path, include
from employee import views  # import your views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('', views.promotion_eligibility, name='root'),  # Map root URL to the promotion eligibility view
]
