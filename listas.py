nomes = ['caio', 'pedro', 'tiberio', 'babi']

pedro = nomes[1]  #pedro

for i in nomes:
    print(i)
    
print( len(nomes) ) #tamanho da lista

#alterar um valor em uma lista

nomes[3] = 'Babilonia'

print(nomes)


#add elementos dentro da lista no final da lista

nomes.append('nome que vai ser excluido jaja')
print(nomes)

#add um elemento em uma posicao especifica,ele n exlui a posicao anterio viu ele so add e aumenta a lista

nomes.insert(4, 'nome escolhido por insert') # o primeiro é a posicao e o segundo paraemtro é o elemnto
print(nomes)


#remover elementos da lista

nomes.pop() #vai exlcuir o utimo valor
print(nomes)

nomes.pop(1) #ele exclui o elemento no indice que vc passa no parametro
print(nomes)

#remove pelo valor e não pelo indice, mas so remove um viss se quiser remover todos mete um for 

nomes.remove('caio') #ele exclui o elemento no indice que vc passa no parametro
print(nomes)


#decobrir o index de um elemento
print(nomes.index('tiberio'))



#ordenar uma lista

listanum2 = [5,8,41,2,35,48,4,564]
print(listanum2)
listanum2.sort() #aqui entra um conceito bacana, vc precisa fazer antes de printar pois certamente ele usar many to many para cria um outra lista
print(listanum2) #vai retornar em odem crescente
listanum2.sort(reverse=True) #assim vai ao contrario(decrescente)
print(listanum2)
 

#se vc não quiser alterar a lista oficial use o metodo sorted 
lista2 = [ 5,1,3 ]
print(sorted(lista2, reverse=True))

#iterando listas enumerando
x = list(range(0,5)) #criar uma lista

x2 = list(enumerate(x)) #enumerando atributos e indices 
print(x2)

############################### LISTA DE LISTAS
lista_de_listas = [[1,2,3],[4,5,6]]

for i in range(0, len(lista_de_listas)):
    print(lista_de_listas[i])
    for j in range(0, len(lista_de_listas[i])):
        print(lista_de_listas[i][j])
        
# LISTA DE LISTAS DE FORMA FUNCIONA 
#list comprehension
X = [[j for j in range(0,3)] for i in range(0,2)] #vc pode criar quantas listas vc quiser é so i olando []
print(X)
    
