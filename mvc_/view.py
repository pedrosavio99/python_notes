
# print(PessoaController.Cadastrar('CAIO',20,'11111111111'))

from unicodedata import decimal
from controller import PessoaController

while True:
    decisao = int(input('digite 1 para salvar \ndigite 2 para ver a pessoa salva\ndigite 3 pra cancelar'))
    if decisao == 1:
        nome = input('digite o nome: ')
        idade = int(input('digite sua idade: '))
        cpf = input('Digite seu cpf: ')
        if PessoaController.Cadastrar(nome, idade, cpf):
            print('Usuario cadastrado')
        else:
            print('valores invalidos')
    elif decisao == 2:
        ...
    else:
        break