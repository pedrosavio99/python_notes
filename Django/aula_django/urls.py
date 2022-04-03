from django.contrib import admin
from django.urls import path, include

from autenticacao import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('', include('index.urls'))  #esse path é so pra evitar aquela pagina de erro 
]
