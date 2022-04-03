#Como criar suas proprias excecoes
#raise KeyError("Deu ruim") #vc pode montar seu erro como quiser chamando esse raise
#muito utilizado em criacao de bibliotecas


#exemplo essa funcao nao pode aceitar numeros negativos
def soma(n1, n2):
    if n1 < 0 or n2 <0:
        raise ValueError('n1 e n2 não podem ser negativos')
    return n1 + n2


print(soma(2,5))


#assert serve para criar comparacoes 
#ex, quero que um numero seja maior que zero se não irei retornar um erro 

x = 5
assert x > 0, "Deu ruim"

