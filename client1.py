import socket, threading, Elgamal

nick= input('Selecciona nombre de usuario: ')

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
f = open("llaves.txt", "r")
pubs = f.read().split(',')
d= 24757538602252597296337232281113767819504967467052861246838036713926834038547
def receive():
    while True:
        try:
            message= client.recv(1024).decode('ascii')
            if message=='Usuario: ':
                
                client.send(nick.encode('ascii'))
            else: 
                
                message= Elgamal.decrypt(message,int(pubs[0]),d)
                print(message)
        except:
            pass
def write():
    while True:
        message= f'{nick}: {input("")}'
        i = Elgamal.eph_key(int(pubs[0]))
        km = Elgamal.M_key(i,int(pubs[4]),int(pubs[0]))
        message2=Elgamal.encrypt(message,km,i,int(pubs[0]),int(pubs[2]))
        client.send(message2.encode('ascii'))

rec_th= threading.Thread(target=receive)
rec_th.start()
wr_th=threading.Thread(target=write)
wr_th.start()