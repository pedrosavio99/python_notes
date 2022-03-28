#FAÇA UM PROGRAMA QUE O USER POSSA CADASTRAR N PESSOAS ( NOME E IDADE )

pessoas = []

while True:
    decisao = int(input('digita 1: cadastrar pessoa -------  2 para sair\n'))
    if decisao == 2:
        break
    
    nome = input('nome : ')
    idade = input('idade : ')
    
    pessoa = {'nome': nome, 'idade': idade}
    pessoas.append(pessoa)
    
    
print(pessoas)