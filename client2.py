import socket, threading, Elgamal

nick= input('Selecciona nombre de usuario: ')

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
f = open("llaves.txt", "r")
pubs = f.read().split(',')
d=39708733867200216092171341556365247557037539255048896527812975873196465733406
def receive():
    while True:
        try:
            message= client.recv(100000).decode('ascii')
            firma=message.split(',')
            if message=='Usuario: ':
 
                client.send(nick.encode('ascii'))
            elif firma[0]=='signature':
                aux = Elgamal.sig_verification(int(firma[1]),int(firma[2]),int(firma[3]),int(pubs[1]),int(pubs[0]),int(pubs[3]))
                if aux == True: 
                    print(Elgamal.decrypt(firma[-1],int(pubs[0]),d))   
        except:
            pass
        
def write():
    while True:
        message= f'{nick}: {input("")}'
        i = Elgamal.eph_key(int(pubs[0]))
        km = Elgamal.M_key(i,int(pubs[3]),int(pubs[0])) # int(pubs[3]) beta cliente 1
        message2=Elgamal.encrypt(message,km,i,int(pubs[0]),int(pubs[1])) # int(pubs[1]) alpha cliente 1
        #firma
        mens=int(message2.replace(" ",""))
        r,s=Elgamal.sig_generation(int(pubs[2]),int(pubs[0]),d,mens)
        signature='signature,'+str(mens)+','+str(r)+','+str(s)+','+str(message2)
        client.send(signature.encode('ascii'))

rec_th= threading.Thread(target=receive)
rec_th.start()
wr_th=threading.Thread(target=write)
wr_th.start()