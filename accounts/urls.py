from django.urls import path

from accounts.views import logout_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
]
