import socket
HOST = 'localhost'
PORT = 8024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #QUAL O SIGNIFICADO DISSO?

sock.bind((HOST,PORT)) #criar server na porta que queremos

sock.listen(5)# isso é a quantidade de clientes que esse server comporta

while True:
    novoSock, _ = sock.accept()
    mensagem = novoSock.recv(1024).decode() #recebe uma msg binaria
    print(mensagem)
    novoSock.send(b'ok, msg recebida')
    novoArquivo = novoSock.recv(1000000)

    with open(f'arquivos/{mensagem}.png','wb') as arq:
        arq.write(novoArquivo)
    
    novoSock.send(b'ok,imagem upada')
