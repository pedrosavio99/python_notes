#sockt em aberto que reenvia essa msg para uma sala 
#vai ter varias threds aparentmente
from concurrent.futures import thread
import socket
import threading


HOST = 'localhost'
PORT = 8031

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()


salas = {} #sala vai ser um dicionpario para podermos adicionar novas salas caso n exista


#BROADCAST  receber essa mensagem e enviar para todo mundo.
def broadcast(sala,mensagem):
    for i in salas[sala]:
        if isinstance(mensagem,str):
            mensagem = mensagem.encode()
        i.send(mensagem)

def enviarMsg(nome,sala,client):  #essa é a segunda thred onde vamos ficar verificando se tem msg nova 
    while True:
        mensagem = client.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n' # aqui ele pega o nome de quem enviou e sua mensagem e enviar pra todo mundo do servidor
        broadcast(sala, mensagem)

while True:     #essa é a primeira thred que fica conectando os clients
    client, addr = server.accept()
    print(client)
    client.send(b'SALA')#aquivou pedir o nome dele e a sala que ele quer entrar
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'{nome} se conectou na sala: {sala}!! info {addr}')   #os clients sao identificados pelo raddr ein
    broadcast(sala, f'{nome}: Entrou na sala!\n')
    thread = threading.Thread(target=enviarMsg, args=(nome, sala, client)) #aqui crio-se o paralelo 
    thread.start() #aqui se ativa ele
