import re
import sys
import hashlib
import operator

# Keys used for the chipers are of size 205
chipher1 = open("challenge1.txt", "rb") # 203 bytes = 203 keys 
chipher2 = open("challenge2.txt", "rb") # 200 bytes = 200 keys
sampleRegex = "^[a-zA-Z0-9_, .-:\"\']*$"

# The first 200 keys used in cipher1 and chiper2 are the same
# In ciphor1 the last 3 keys are not of any used in ciphor1

def x_or_chipers():
    content1 = chipher1.read()
    content2 = chipher2.read()
    xor_content = bytearray(200)

    for i in range(200):
        xor_content[i] = content1[i] ^ content2[i]

    return xor_content


def guess_word1(guess_word1):
    guess_word1_as_bytes = guess_word1.encode("ISO-8859-1")
    try_word(guess_word1_as_bytes)


def try_word(guess_word_as_bytes):
    byte_array_xor = x_or_chipers()
    byte_array_readable_output = bytearray(len(guess_word_as_bytes))
    
    for slide_len in range(len(byte_array_xor) - len(guess_word_as_bytes)):
        for i in range(len(guess_word_as_bytes)):
            byte_array_readable_output[i] = guess_word_as_bytes[i] ^ byte_array_xor[i+slide_len]       
        readable_output_as_string = byte_array_readable_output.decode("ISO-8859-1")
        if re.match(sampleRegex, readable_output_as_string):
            print("slide = " , slide_len , "readable string = " , readable_output_as_string)        


def print_list():
    cracked_words = open("cracked.txt", "r")
    c1chars = []
    c2chars = []
    i = 0  
    for line in cracked_words:
       c1chars.append(line[4])
       c2chars.append(line[11])
       i = i + 1
    print("Printing line c1")
    for char in c1chars:
        print(char, end = '')
    print("\n")
    print("printing line c2")
    for char in c2chars:
        print(char, end = '')


def fetch_c1():
    cracked_words = open("cracked.txt", "r")
    c1chars = []
    i = 0  
    for line in cracked_words:
       c1chars.append(line[4])
       i = i + 1
    return c1chars


def fetch_c2():
    cracked_words = open("cracked.txt", "r")
    c2chars = []
    i = 0  
    for line in cracked_words:
       c2chars.append(line[11])
       i = i + 1
    c2chars.pop()
    c2chars.pop()
    c2chars.pop()
    return c2chars


def sha256sum():
    cracked_plainText_c1 = listToString(fetch_c1())
    cracked_plainText_c2 = listToString(fetch_c2())
    encryption_key = calc_encryption_key()
    cracked_cypher_1 = encrypt_otp(encryption_key,cracked_plainText_c1)
    cracked_cypher_2 = encrypt_otp(encryption_key,cracked_plainText_c2)

    hashedValue_c1 = hashlib.sha256(cracked_cypher_1.encode("ISO-8859-1")).hexdigest()
    hashedValue_c2 = hashlib.sha256(cracked_cypher_2.encode("ISO-8859-1")).hexdigest()
    print(hashedValue_c1)
    print(hashedValue_c2)

    if("fdb8bb2642cb7c9a1869ab99019e3ee3eaff5160c0cf5c8aec1267742e941eb1" == hashedValue_c1):
        print("Challenge1.txt ciphertext matches hash value")
    if("44e79e85e1aaa37ba74a4a77a7fb15f2da43bca494f1b6ff3ab3eb493b68c24f" == hashedValue_c2):
        print("Challenge2.txt ciphertext matches hash value")
  

# Calculate the encryption key by brute force
# Give the plaintext and the cypher, we can to find the key
def calc_encryption_key():
    chipher1 = open("challenge1.txt", "rb") # 203 bytes = 203 keys 
    plainText = fetch_c1()
    keys = []

    chipher1_read = chipher1.read()

    for charCounter in range(len(plainText)):
        for i in range(255):
            guessCypher = ord(plainText[charCounter]) ^ i
            if(guessCypher == chipher1_read[charCounter]):
                keys.append(i)  
    return keys


def encrypt_otp(keys,plaintext):
    cypher_text = []
    item_counter = 0
    for item in plaintext:           
        cypher_text.append(chr(ord(item) ^ keys[item_counter]))
        item_counter =  item_counter + 1
    cypher_string = ""
    return cypher_string.join(cypher_text)


# Function to convert   
def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1


if __name__ == "__main__":
    #print(x_or_chipers())
    #word = sys.argv[1]
    #guess_word1(word)
    #print_list()
    #print(fetch_c1())
    #print(fetch_c2())
    sha256sum()
    #cypher_keys = calc_encryption_key()
    #plainText = fetch_c1()
