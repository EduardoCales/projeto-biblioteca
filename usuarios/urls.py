from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name="cadastro"),
    path('cadastro/create/', views.cadastro_create, name="create"),
]
