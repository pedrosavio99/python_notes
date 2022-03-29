#serializar significa pegar algo que esta em memoria e tornar persistente

import pickle #usado para serializar

#dumps vai apeas retornar a strign binaria

#dump vai salvar em um arquivo

#o pickle n esta criptografando viu se ligue

x = [1,2,3]
binario = pickle.dumps(x) #aqui é o dado em memoria em formato de binario
print(binario)

print(pickle.loads(binario)) #aqui retorna ao valor inicial


#COMO SALVAR ESSE BINARIOS EM SUA MAQUINA 

lista = [ 1,2,3 ]
arq = open('arquivo_salvar_serializados.pkl','wb') #aqui eu abro o arquivo que vou salvar os binario e vou esrever o arquivo em binario wb
pickle.dump(lista, arq)

#abrir o arquivo em modo de leitura e ver oq salvou
arq = open('arquivo_salvar_serializados.pkl','rb')
retorno = pickle.load(arq)

print(retorno , "esse ja voltou do arquivo binario")

