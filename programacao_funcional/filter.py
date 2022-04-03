#o filter recebe dois parametros uma funcao e um retorno

x = [1,2,3,4]
#      depois do lambda o primeiro x é o parametro
#     o segundo é as comparacoes e o terceiro x é a propria lista
x = list(filter(lambda x: x < 3, x))


#aqui filtrou todos os numeros menor que 3
print(x)