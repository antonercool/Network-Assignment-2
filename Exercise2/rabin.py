#To carefully generate random number we use the secrets library
# https://docs.python.org/3.6/library/secrets.html
# Large Prime Generation for RSA 
#https://www.geeksforgeeks.org/rabin-cryptosystem-with-implementation/
from Cryptodome.Util import number
from Cryptodome import Random
import Cryptodome
import codecs
import sys
  
#Generate primes using Cryptodome
def generate_primes(bitsize):
    while True:
        p = number.getPrime(bitsize, randfunc=Cryptodome.Random.get_random_bytes)
        q = number.getPrime(bitsize, randfunc=Cryptodome.Random.get_random_bytes)
        ## Make sure the big primes are not equal + ensure 
        if (p != q) and ((p % 4) ==3) and ((q % 4)==3):
            return (p,q)

def generate_public_key(p, q):
    return p * q

def encrypt_message(public_key, message):
    return message**2 % public_key      

def encode_message(message):
    hex_acum = "0x"
    # do twice for padding
    for i in range(2):
        for charactor in message:
            hex_acum += str(hex(ord(charactor)))[2:]

    message_as_value = int(hex_acum, 16)
    return message_as_value


def is_correct_message(message_as_value):
    message_as_bytes = int_to_bytes(message_as_value)
    message_size = int(len(message_as_bytes)/2)
    is_corret = True 
    for i in range(message_size):
        if message_as_bytes[i] == message_as_bytes[i+message_size] :
            is_corret &= True
        else:
            is_corret &= False

    return is_corret

def fetch_correct_message(decrypted_tuple):
    for message in decrypted_tuple:
        if is_correct_message(message):
            return message


# https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def decode_message(value):
    string_acum = ""
    value_as_hex = codecs.encode(int_to_bytes(value), "hex").decode("utf-8")  
    raw_bytes = bytes.fromhex(value_as_hex)
    for i in range(int(len(raw_bytes)/2)):
        string_acum += chr(raw_bytes[i])

    return string_acum

# https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
def gcd_extended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
    gcd,x1,y1 = gcd_extended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def egcd(a,b):   
    s1, s2 = 1, 0   
    t1, t2 = 0, 1   
    while b!=0:   
        q = a//b    
        r = a%b   
        a, b = b, r     
        s = s1 - (q*s2)    
        s1, s2 = s2, s      
        t = t1 - (q*t2)    
        t1, t2 = t2, t    
    return (s1, t1)    
      

def decrypt_message(encrypted_message, p, q, n):
    # Find yp and yq with extended Eucildean algorithm
    egcd_tuple = egcd(p, q)
    yp = egcd_tuple[0]
    yq = egcd_tuple[1]
    #Compute the square root of c modulo p and q
    if (yp*p+yq*q) != 1:
        print("ERROR!")
    mp = pow(encrypted_message, (p + 1) // 4, p)
    mq = pow(encrypted_message, (q + 1) // 4, q)

    #Chinese remainder theorem 
    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * mq - yq * q * mp) % n
    r4 = n - r3
    return r1, r2 , r3, r4
  
if __name__ == '__main__': 
    message = sys.argv[1]
    bit_size = 256
    primetuple = generate_primes(bit_size)
    
    p = primetuple[0]
    q = primetuple[1]
    n = generate_public_key(q,p)
    print("Keys for encryption : ")
    print("\t p : " , p )
    print("\t q : " , q )
    print("\t n : " , n )

    encoded_message = encode_message(message)
    print("Preparing text for encrypting -- encoding")
    print("Encoded messsage with padding :", encoded_message)
    encrypted_message = encrypt_message(n, encoded_message)
    
    print("Encrypted messsage :" ,encrypted_message)
    decrypted_message = decrypt_message(encrypted_message, p, q, n)

    i = 1
    for cipher in decrypted_message:
        print("decrypted chiper nr :", i , " = ", cipher) 
        i = i + 1

    print("\t fecthing correct decryptet cipher..")
    
    final_message = fetch_correct_message(decrypted_message)
    print("final raw text : " ,decode_message(final_message) )

