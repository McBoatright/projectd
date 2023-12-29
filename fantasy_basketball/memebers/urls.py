from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('memebers/', views.memebers, name='memebers'),
    path('memebers/details/<int:id>', views.details, name='details'),
]