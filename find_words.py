import re
import sys
import hashlib

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
       c1chars.append(line[13])
       c2chars.append(line[20])
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
       c1chars.append(line[13])
       i = i + 1
    return c1chars

def fetch_c2():
    cracked_words = open("cracked.txt", "r")
    c2chars = []
    i = 0  
    for line in cracked_words:
       c2chars.append(line[20])
       i = i + 1
    c2chars.pop()
    c2chars.pop()
    c2chars.pop()
    return c2chars

def sha256sum():
    #44e79e85e1aaa37ba74a4a77a7fb15f2da43bca494f1b6ff3ab3eb493b68c24f  
    #fdb8bb2642cb7c9a1869ab99019e3ee3eaff5160c0cf5c8aec1267742e941eb1
    #   
    #d51b39f1ac07f0a65f30c19622d691d5ad99ba8aa7300d925db5afc83f9e77e1
    #d2a7f30b54ba614132bbbaa22a064051c8460f09acaa5df3869b1ac07a954d4c

    plainText_c1 = listToString(fetch_c1())
    plainText_c2 = listToString(fetch_c2())
    test = "\"Taken in its entirety, the Snowden archive led to an ultimately simple conclusion: the US government had built a system that has as its goal the complete elimination of electronic privacy worldwide."

    hashedValue_c1 = hashlib.sha256(test.encode("ISO-8859-1")).hexdigest()
    hashedValue_c2 = hashlib.sha256(plainText_c2.encode("ISO-8859-1")).hexdigest()
    #print(hashedValue_c1)
    print(hashedValue_c2)

    if("fdb8bb2642cb7c9a1869ab99019e3ee3eaff5160c0cf5c8aec1267742e941eb1" == hashedValue_c1):
        print("Challenge1.txt ciphertext matches hash value")

    if("44e79e85e1aaa37ba74a4a77a7fb15f2da43bca494f1b6ff3ab3eb493b68c24f" == hashedValue_c2):
        print("Challenge1.txt ciphertext matches hash value")

        
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
    sha256sum()

