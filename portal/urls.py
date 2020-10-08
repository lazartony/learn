from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portal_home'),
    path('login/', views.login, name='portal_login'),
]