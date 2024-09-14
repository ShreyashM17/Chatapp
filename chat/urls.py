from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration),
    path('<str:name>/', views.lobby),
    path('<str:name>/logout', views.logout)
]