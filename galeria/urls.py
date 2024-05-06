from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('oi/', views.inicio_view, name='inicio_view'),
    path('login/', views.login, name='login'),
    path('seguranca/', views.seguranca, name='seguranca')
]