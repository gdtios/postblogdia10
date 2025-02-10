from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('novo/', views.criar_post, name='criar_post'),
]
