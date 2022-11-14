import Elgamal

if __name__=='__main__':
    #El orden es el siguiente: [Primo, Alpha1, Alpha2, Beta1, Beta2]
    k=[]
    p=Elgamal.find_prime(256)
    k.append(p)
    alp1=Elgamal.find_primitive_root(p)
    alp2=Elgamal.find_primitive_root(p)
    k.append(alp1)
    k.append(alp2)
    d1 = Elgamal.priv_key(p)
    d2= Elgamal.priv_key(p)

    be1=Elgamal.pub_key(alp1,d1,p)
    be2=Elgamal.pub_key(alp2,d2,p)
    k.append(be1)
    k.append(be2)

    k=str(k)
    k=k.replace('[', '')
    k=k.replace(']', '')
    with open("llaves.txt", "w") as f:
        f.write(k)

    print("Llaves privadas!! \n", f'{d1}, {d2}')