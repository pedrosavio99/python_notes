from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro), #essa funcao vai fazer uma requisicao e vai receber um response
    path("", views.auth),
    path('login/', views.login)
]
