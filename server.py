import socket, threading, Elgamal

serv_ad= '127.0.0.1'
puerto= 55555

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((serv_ad, puerto))
server.listen()

clients=[]
nicks=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message= client.recv(100000)
            broadcast(message)
        except:
            idx= clients.index(client)
            clients.remove(client)
            client.close()
            nick= nicks[idx]
            nicks.remove(nick)
            break

def receive():
    print("Estamos activos!")
    while True:
        
        client, addr= server.accept()
        print(f"Se conectó: str({addr})")
        client.send("Usuario: ".encode('ascii'))
        nick= client.recv(100000).decode('ascii')
        nicks.append(nick)
        clients.append(client)
        #broadcast(f"{nick} se ha conectado!".encode('ascii'))
        thread=threading.Thread(target=handle,args=(client,))

        thread.start()
            
receive()
