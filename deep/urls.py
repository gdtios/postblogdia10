from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de URL para a página inicial da app
    path('chatdeep/', views.chat, name='chatdeep'),  # Exemplo de URL para uma página de chat
]