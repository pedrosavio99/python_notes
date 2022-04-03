import socket
HOST = 'localhost'
PORT = 8024

#criar arqquivo ou receber de um front
arquivo = open('img.png','rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criar conexao

sock.connect((HOST,PORT))

sock.send(input('Digite sua msg para o srver, ou melhor nome do arquivo: ').encode()) #esse encode vai tranformar em binario se quiser descodar mnada um decode()
    #b'teste cliente')# esse b converte em binario
sock.send(arquivo.read())

confirmacao_recebida = sock.recv(1024)

if confirmacao_recebida == b'ok, msg recebida':
    print ('msg enviada!! e o server respondeu')