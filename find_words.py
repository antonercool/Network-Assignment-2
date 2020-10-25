# Keys used for the chipers are of size 205
chipher1 = open("challenge1.txt", "rb") # 203 bytes = 203 keys 
chipher2 = open("challenge2.txt", "rb") # 200 bytes = 200 keys

# The first 200 keys used in cipher1 and chiper2 are the same
# In ciphor1 the last 3 keys are not of any used in ciphor1


def x_or_chipers():
    content1 = chipher1.read()
    content2 = chipher2.read()
    xor_content = bytearray(200)

    for i in range(200):
        xor_content[i] = content1[i] ^ content2[i]


    return xor_content

def guess_word1():

    guess_word1 = "for people around the world with"
    guess_word1_as_bytes = guess_word1.encode("ISO-8859-1")
   
    try_word(guess_word1_as_bytes)
    
def try_word(guess_word_as_bytes):
    byte_array_xor = x_or_chipers()
    byte_array_readable_output = bytearray(len(guess_word_as_bytes))
    
    for slide_len in range(len(byte_array_xor) - len(guess_word_as_bytes)):
        for i in range(len(guess_word_as_bytes)):
            byte_array_readable_output[i] = guess_word_as_bytes[i] ^ byte_array_xor[i+slide_len]       
        readable_output_as_string = byte_array_readable_output.decode("ISO-8859-1")
        print("slide = " , slide_len , "readable string = " , readable_output_as_string)




def print_list():
    listSize = 203
    for i in range(listSize):
        print(i , " --  C1:  " , "C2:  " )
        
if __name__ == "__main__":
    #print(x_or_chipers())
    #guess_word1()
    print_list()

# Word list
# Whe  61, As, 128, this 142, " has a" internet 70

#english 141
# " around the world" 121  - guess "ilt a system that has as its goal to"
# "m that has" 110 - guess " for people around the world with"


#def string_to_hex(str):
#    return hex(int(str,base=16))    

#def count_chipher():
#    content = chipher1.read()
#    for elem in content:
#            if elem in chipherDict:
#                    chipherDict[elem] = chipherDict[elem] + 1
#            else:
#                chipherDict[elem] = 1
#    for item in chipherDict.items():
#        print(item)             
#
#            #countOfElem = content.count(elem)
#            #print("char " , elem  , " nr : " , countOfElem)
#    ##print(content)
#    chipher1.close()




