#while e for

#while quando n sabemos a quantidade

#for pra quand sabemos a quantidade de vezes que queremos repetir

i = 0 #contador
while i < 10:
    print(i)
    if i%2 == 0:
        i = i + 2
        continue #isso daqui faz com que o programa volte para o laço e n rode o resto
    if i == 5:
        break #omando para quebrar um laço
    i += 1
    
    

x = [1,2,3]
for i in x:
    print(i)
    
    
n1 = 5  
for i in range(1,11): #é sempre o ultimo que vc quer mais 1 
    print(f'{n1} x {i} = {n1 * i}')
    
n1 = 5  
for i in range(0,101,5): #esse terceiro parametro é o step pra pular casas
    print(i)
    
#fr aninhados 

for i in range(1,3):
    for j in range(1,3):
        print(f'i = {i} j = {j}')