from django.urls import path

from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.home, name="home"),
    path('livros/category/<int:category_id>/', views.category, name="category"),
    path('livros/<int:id>/', views.livro, name="livro"),
]