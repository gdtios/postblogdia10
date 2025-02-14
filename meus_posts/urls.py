from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('novo/', views.criar_post, name='criar_post'),
    path('blank/', views.blank_page, name='blank_page'),
    path('chat/', 
         views.minha_view_rag_perplexity, name='blank_page'),
    
    
]

