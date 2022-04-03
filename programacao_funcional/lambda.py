#uma funcao mais curta e de forma mais simples

from cgi import test


x = lambda *args : print(args)
x(3,3,3)


#podemos usar uma lambd como retorno de uma funcao

def teste(n1):
    if n1%2 == 0:
        a = n1*2
        z = lambda a : 'pedosalvo' #def = z , lambda = def e o que vem depois do : é o return
        return z(a)
    else:
        return ('Numero impar')

print(teste(2))

