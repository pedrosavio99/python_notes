from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def auth(requests):
    return HttpResponse('bem vindo a minha api !')