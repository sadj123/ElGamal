import random
import math

# Se trabajara con una contraseña de 256 bits para mas seguridad 
#=====================================================================================================
# Paso 1 encontrar un numero primo muy grande 
#=====================================================================================================

# Test de primalidad de miller Rabin 
def miller_rabin(n):

    if n == 2 or n==1 or n==3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(7):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_prime(Bits):
		while(1):
                # generamos un numero aleatorio 
				p = random.randint( 2**(Bits-2), 2**(Bits-1) )
                # revisamos que no sea par 
				while( p % 2 == 0 ):
						p = random.randint(2**(Bits-2),2**(Bits-1))

				# Nos aseguramos con el test de primalidad del Miller Rabin
				while( not miller_rabin(p) ):
						p = random.randint( 2**(Bits-2), 2**(Bits-1) )
						while( p % 2 == 0 ):
								p = random.randint(2**(Bits-2), 2**(Bits-1))
				p = p * 2 + 1
				if miller_rabin(p):
						return p

#=====================================================================================================
# Paso 2 encontrar un generador del grupo 
#=====================================================================================================
def find_primitive_root(p):
		if p == 2:
				return 1
		p1 = 2
		p2 = (p-1) // p1
		while( 1 ):
				g = random.randint( 2, p-1 )
				if not (pow( g, (p-1)//p1, p ) == 1):
						if not pow( g, (p-1)//p2, p ) == 1:
								return g

#=====================================================================================================
# Paso 3 Escoger un llave privada entre [2,p-2]
#=====================================================================================================
def priv_key(p):
    d = random.randint(2, p-2)
    return d

#=====================================================================================================
# Paso 4 Calcular la llave publica
#=====================================================================================================
def pub_key(alpha,d,p):
    return pow(alpha,d,p)
# Llave efiemra
def eph_key(p):
    i = random.randint(2, p-2)
    return i 
#=====================================================================================================
# Paso 5 llave de enmascaramiento 
#=====================================================================================================
def M_key(i,beta,p):
    
    K_M=pow(beta,i,p)
    return  K_M

#=====================================================================================================
# Paso 6 Encriptamos 
#=====================================================================================================
# Funcion que codifica el mensaje de exa a bytes tomando cada bit
def encode(sPlaintext):
		byte_array = bytearray(sPlaintext, 'utf-16')		
		z = []
		k = 256//8
		j = -1 * k
		for i in range( len(byte_array) ):
				if i % k == 0:
						
						j += k
						z.append(0)
				z[j//k] += byte_array[i]*(2**(8*(i%k)))
		return z
    
def encrypt(x,km,y,p,alpha):
    z = encode(x)
    cipher_pairs = []
    for i in z:
            # llave efimera
            c = pow( alpha, y, p )
            # Texto cifrado
            d = (i*km) % p
            cipher_pairs.append( [c, d] )

    encryptedStr = ""
    for pair in cipher_pairs:
        encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '
	
    return encryptedStr

#=====================================================================================================
# Paso 7 Desencriptamos 
#=====================================================================================================
def decode(aiPlaintext):
		bytes_array = []
		k = 256//8
		for num in aiPlaintext:
				for i in range(k):
						temp = num
						for j in range(i+1, k):							
								temp = temp % (2**(8*j))
						letter = temp // (2**(8*i))
						bytes_array.append(letter)
						num = num - (letter*(2**(8*i)))
		decodedText = bytearray(b for b in bytes_array).decode('utf-16')
		return decodedText

def decrypt(cipher,p,x):
		plaintext = []

		cipherArray = cipher.split()
		if (not len(cipherArray) % 2 == 0):
			return "texto malformado"	
		for i in range(0, len(cipherArray), 2):
				c = int(cipherArray[i])
				d = int(cipherArray[i+1])
				s = pow( c, x, p )
				plain = (d*pow( s, p-2, p)) % p
				plaintext.append( plain )
		decryptedText = decode(plaintext)
		decryptedText = "".join([ch for ch in decryptedText if ch != '\x00'])
		return decryptedText

#=====================================================================================================
# FIRMA DIGITAL ELGAMAL
#=====================================================================================================
#=====================================================================================================
# Paso 1 generacion de la firma
#=====================================================================================================
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def sig_generation(alpha,p,d,x):
    while True:
        ke=random.randint(2, p-2)
        if math.gcd(ke,p-1)==1:
            break
    inv_ke=modinv(ke,(p-1))
    r=pow(alpha,ke,p)
    s=((x-(d*r))*inv_ke)%(p-1)
    if s == 0:
        sig_generation(alpha,p,d,x)
    else:
        return (r,s)

#=====================================================================================================
# Paso 2 verificacion de la firma 
#=====================================================================================================

    
def sig_verification(x,r,s,alpha,p,beta):
    t = (pow(beta,r,p)*pow(r,s,p))%p
    if t == pow(alpha,x,p):
        return True
    else:
        return False


    