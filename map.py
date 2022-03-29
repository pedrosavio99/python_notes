#diferente do filter que  filtra dados em uma lista o map vai modificar valores em uma filtragem


#criando uma lista
x = [i for i in range(15,26)]

#todos os valores menor que 18 iráo se tornar 10
x = list(map(lambda x : 10 if x < 18 else(x), x))

print(x)

#outro exemplo
x = [{'nome':'pedro','idade':5},{'nome':'pedro2','idade':5}]
print(x)

#aqui eu modifico a idade de cada elemento do dicionpario com a chave idade menor que 18 para a idade 24
x = list(map(lambda x : {'nome': x['nome'],'idade':22} if x['idade'] < 10 else(x), x))

print(x)