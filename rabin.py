#To carefully generate random number we use the secrets library
# https://docs.python.org/3.6/library/secrets.html
# Large Prime Generation for RSA 
#https://www.geeksforgeeks.org/rabin-cryptosystem-with-implementation/
from Cryptodome.Util import number

""" Encryption
1. Get the public key n.
2. Convert the message to ASCII value. 
Then convert it to binary and extend the binary value with itself,
 and change the binary value back to decimal m.
3. Encrypt with the formula:C = m2 mod n
4. Send C to recipient. """
def encryption(public_key, message):
    #array2 = bytes(message, 'ascii')
    #int_value = int.from_bytes(array2, byteorder='little', signed=True)
    message_padded = padding(message)
    return (message_padded**2) % public_key  

def padding(message):
    binary_str = bin(message)     # convert to a bit string
    output = binary_str + binary_str[-16:]      # pad the last 16 bits to the end
    return int(output, 2)       # convert back to integer

def decryption(encrypted_message, p, q, n):
    egcd_tuple = egcd(p, q)
    # Find yp and yq with extended Eucildean algorithm
    yp = egcd_tuple[0]
    yq = egcd_tuple[1]
    #Compute the square root of c modulo p and q
    mp = fast_pow(encrypted_message, (p + 1) / 4, p)
    mq = fast_pow(encrypted_message, (q + 1) / 4, q)
    #Chinese remainder theorem 
    lst = [r1, r2, r3, r4]
    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * mq - yq * q * mp) % n
    r4 = n - r3
    return r1, r2 , r3, r4

    plaintext = choose(lst)
    string = bin(plaintext)
    string = string[:-16]
    plaintext = int(string, 2)

    return plaintext
    #print('This is a:', a, "\n" , "This is b:", b, "\n", "This is r:", r, "\n", "This is s:", s)

def choose(lst):
    for i in lst:
        binary = bin(i)

        append = binary[-16:]   # take the last 16 bits
        binary = binary[:-16]   # remove the last 16 bits

        if append == binary[-16:]:
            return i
    return

def fast_pow(num, power, mod):
    #result
    res = 1 
    # (b ^ k) * p = num ^ power
    while power > 0:
        while power % 2 == 0:
            power /= 2
            num = (num * num) % mod
        power -= 1
        res = (res * num) % mod
    return res   

#Generate primes using Cryptodome
def generate_primes(bitsize):
    p = number.getPrime(bitsize)
    while True:
        q = number.getPrime(bitsize)
        if (p != q):
            return (p,q)

def generate_public_key(p, q):
    return p * q



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




if __name__ == '__main__': 
    message = "hello"
    plaintext =  number.bytes_to_long(message.encode('utf-8'))
    bit = 256
    primetuple = generate_primes(bit)
    #p = primetuple[0]
    p = 270576397968349702240268570806789986947
    #q = primetuple[1]
    q = 219242991039694982252977037582947245671
    #n = generate_public_key(p, q)
    n = 59321978795327837368543975705006433832257716767865371948246597234695692256437
    encrypted_message = encryption(n, plaintext)
    print(encrypted_message)
    decrypt_tuple = decryption(encrypted_message, p, q, n)
    for x in decrypt_tuple:
        bytestest = x.to_bytes(100, byteorder='little')
        print(str(bytestest, 'ISO-8859-1'), "\n")


        


""" Decryption
1. Accept C from sender.
2. Specify a and b with Extended Euclidean GCD such that, a.p + b.q = 1
3. Compute r and s using following formula:
r = C(p+1)/4 mod p
s = C(q+1)/4 mod q
4. Now, calculate X and Y using following formula:
X = ( a.p.r + b.q.s ) mod p
Y = ( a.p.r – b.q.s ) mod q
5. The four roots are, m1=X, m2=-X, m3=Y, m4=-Y
Now, Convert them to binary and divide them all in half.
6. Determine in which the left and right half are same. Keep that binary’s one half
 and convert it to decimal m. Get the ASCII character 
 for the decimal value m. The resultant character gives the correct message sent by sender.
 """

 