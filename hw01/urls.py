from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='Главная'),
    path('about/', views.about, name='О себе'),
    ]