from traceback import print_tb


n1 = float(input('nota 1 : \n'))
n2 = float(input('nota 2 : \n'))
n3 = float(input('nota 3 : \n'))
n4 = float(input('nota 4 : \n'))

media = (n1 + n2 + n3 + n4)/4

if media >=6:
    print(f'Aprovado {media}')
elif media >= 4:
    print(f'recuperacao {media}')
else:
    print(f'reprovado {media}')