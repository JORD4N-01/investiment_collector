from django.urls import path

from . import views

urlpatterns = [
    path('app/', views.app_home, name='app_home'),
]
