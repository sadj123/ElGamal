# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:39:24 2022

@author: gianc
"""

import Elgamal

"""
PENDIENTES: ECOGER ALEATORIAMNETE LA LLAVE EFIMERA 
"""
def main():
    # Texto a cifrar 
    texto="wenas"
    # encontramos numero primo de 256 bits
    p = Elgamal.find_prime(256)
    # encontramos un generador del grupo Z_p
    alpha = Elgamal.find_primitive_root(p)
    # llave privada y llave efimera 
    d,i = Elgamal.priv_key(p)
    # calculamos beta 
    beta=Elgamal.pub_key(alpha,d,p)
    #  calculamos km
    km = Elgamal.M_key(i,beta,p)
    # ciframos el mensaje 
    msg_enc = Elgamal.encrypt(texto,km,i,p,alpha)
    #deciframos el mensaje
    print(Elgamal.decrypt(msg_enc,p,d))
    
    
    
    
    # verificacion usando la firma digital
    #x,r,s=Elgamal.sig_generation(alpha,p,d,int(msg_enc.replace(" ","")))

    
    #print(t==pow(alpha,x,p))
    #print(Elgamal.sig_verification(int(msg_enc.replace(" ","")),r,s,alpha,p,beta))
if __name__=='__main__':
    t= input("Ingrese texto a cifrar: ")
    p = Elgamal.find_prime(256)
    alpha = Elgamal.find_primitive_root(p)
    d,i = Elgamal.priv_key(p)
    beta=Elgamal.pub_key(alpha,d,p)
    km = Elgamal.M_key(i,beta,p)
    msg_enc = Elgamal.encrypt(t,km,i,p,alpha)
    print("Texto a cifrar: ", t)
    print("El mensaje cifrado es: ", msg_enc)
    print("Mensaje decifrado: ", Elgamal.decrypt(msg_enc,p,d))