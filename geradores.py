#funcoes geradoras proveem oq voce quer e são inumeras vezes mais eficiente em gasto de memoria

def dobro (lista):
    for i in lista:
        #print(i)
        yield i*2


x = dobro(range(0,1000000000))
for i in x:
    print(i)


#isso é errado
# while True:
#     print(next(x))