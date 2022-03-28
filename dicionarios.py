x = {'nome':'pedro','idade':22}
print(x)
print(x['nome'])


#ussando listas dentro de dicionários


x = {'nomes': [],'idade':22}

x['nomes'].append('pedroooo')
x['nomes'].append('pedroooo2')
print(x) #o contrario tbm é valido, isto é, é ossivel criar lista om dicionários dento

#atualizar ou add campus no dicionario

p = {'a':1, 'b':2}
print(p)
p.update({'c':3,'d':4})
print(p)

#chaves e valores de um dicionarios

print(p.values())
print(p.keys())

for i in p.items(): #iterando um dicionário
    print(i)