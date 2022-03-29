from asyncore import read


arquivo = open('arquivo.txt', 'w')

#como escrver nele ele sempre vai sobrescrever seu arquivo

arquivo.write('teste1')
arquivo.close()


arquivo = open('arquivo.txt', 'a')
arquivo.write('\n teste2 \n')
arquivo.close()


with open('arquivo2.txt','w') as arq: #usamos esse with para evitar por o close nos codigs
        arq.writelines('teste1')
        arq.writelines('\n')

i = 0     
while True:
        if i > 3:
                break
        arquivo = open('arquivo.txt', 'a')
        arquivo.write(input('digie um nome para ser salvo: \n'))
        arquivo.write('\n')
        arquivo.close()
        i += 1
        
#ler o arquivo

arquivo = open('arquivo.txt', 'r')
rsultado = arquivo.readlines()
arquivo.close()

for i in rsultado:
        print(i)
        
        
#como separar seus dados

x = []
for i in rsultado:
        x.append(i.split())

print(x)


