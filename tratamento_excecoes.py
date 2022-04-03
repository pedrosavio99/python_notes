n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

try:
    print(n1/n2)
except:
    print('Não consegui')
finally:
    print('Finalizado')


#tratamento especializado 

try: 
    x = int(input('Digite um numero: '))
    print(5/x)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0!')
except Exception as e:
    print(f'erro: {e}')



#erro padrao em arquivos de log
