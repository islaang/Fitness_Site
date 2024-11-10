from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('clothing/', views.clothing, name='clothing'),
    path('workouts/', views.workouts, name='workouts'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('cart/', views.cart, name='cart'),
]
