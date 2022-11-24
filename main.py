import Elgamal

def main():
    # Texto a cifrar 
    texto="Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando.Hola como estas, yo la he pasado muy bien pero tu como que no. Porfa no me ignores cuando te estoy hablando."
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
    r,s=Elgamal.sig_generation(alpha,p,d,mens)
    print(Elgamal.sig_verification(mens,r,s,alpha,p,beta))
main()
