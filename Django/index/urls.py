from django.urls import path, include
from . import views

urlpatterns = [
#essa funcao vai fazer uma requisicao e vai receber um response
    path("", views.auth),

]
