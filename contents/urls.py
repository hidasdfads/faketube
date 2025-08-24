from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('channel/<int:channel_id>/', views.home, name="channel_detail"),
]

