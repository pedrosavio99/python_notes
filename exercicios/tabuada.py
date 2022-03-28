n1 = int(input('Digite um numero para tabuada de multiplicacao: \n'))

i = 1
while i <=10:
    print(f'{n1} x {i} = {n1 * i}')
    i += 1
    
#nesse exemplo o mais facil é e correto com for 

for i in range(1,11): #é sempre o ultimo que vc quer mais 1 
    print(f'{n1} x {i} = {n1 * i}')
    