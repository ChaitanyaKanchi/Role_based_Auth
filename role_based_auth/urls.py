from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
