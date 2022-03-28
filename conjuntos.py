#conjunto é atribuido pelo set e ele n permi dados repetidos

x = [1,1,2,3]
print(x)

x = set(x) #removera os repetidos pois virou um conjuntos
print(x)

#unir conjuntos

c1 = [1,2,3]
c2 = [3,4,5]
c1 = set(c1)
c2 = set(c2)
uniao = c1.union(c2) #ira ignorar o 3 pois é repetido

print(uniao)


#intersecao entre dis conjuntos

print( c1.intersection(c2))

#difeença entre dois cojuntos

print(c1.difference(c2))