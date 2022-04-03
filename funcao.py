#dividir pra conquistar sempre divida seus problemas em pequenas partes



#pegar todos os parametros de uma funcao

from cgi import test


def my_function(*args):
    print(args)

my_function(1,21,21,2,99,32,3,2)

#agr posso passar um argumento e outros valores pra um args

def soma_numeros(n1,n2,*args):
    print(n1+n2)
    print(args)


soma_numeros(1,21,21,2,99,32,3,2)

#Kwargs é a forma de passar atributos na forma de chave e valor tipo um dict

def soma_numeros2(**kwargs):
    x = kwargs.get('teste1')
    if x:
        print(f'foi passado! {x}')
    else:
        print('não foi pssao')

soma_numeros2(teste1 = 'testaaando123')


#retornando valores para podermos acessar como variavel

def soma_valores(n1,n2):
    print(n1 + n2)
    return(n1 + n2) #adcionando esse return podemos acessar o retorno em variaveis 

y = soma_valores( 1,2 )

print(y)