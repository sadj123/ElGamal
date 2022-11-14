import Elgamal

def main():
    # Texto a cifrar 
    texto="wenas este es otro texto de prueba"
    # encontramos numero primo de 256 bits
    p = Elgamal.find_prime(256)
    # encontramos un generador del grupo Z_p
    alpha = Elgamal.find_primitive_root(p)
    # llave privada y llave efimera 
    d = Elgamal.priv_key(p)
    #print("x es: ", )
    i = Elgamal.eph_key(p)
    # calculamos beta 
    beta=Elgamal.pub_key(alpha,d,p)
    #  calculamos km
    km = Elgamal.M_key(i,beta,p)
    # ciframos el mensaje 
    msg_enc = Elgamal.encrypt(texto,km,i,p,alpha)
    #deciframos el mensaje
    print(Elgamal.decrypt(msg_enc,p,d))
    
    
    
    
    # verificacion usando la firma digital
    mens=int(msg_enc.replace(" ",""))
    x,r,s,ke=Elgamal.sig_generation(alpha,p,d,mens)
    print(Elgamal.sig_verification(x,r,s,alpha,p,d,ke))
main()
