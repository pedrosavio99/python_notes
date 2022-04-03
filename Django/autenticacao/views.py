from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(requests):
    return HttpResponse('Faça seu cadastro')

def login(requests):
    return HttpResponse('Faça seu login')

def auth(requests):
    return HttpResponse('vc esta na pagina de autenticacao \ndigite na url cadastro/ ou login/')