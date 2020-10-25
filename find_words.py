import re
# Keys used for the chipers are of size 205
chipher1 = open("challenge1.txt", "rb") # 203 bytes = 203 keys 
chipher2 = open("challenge2.txt", "rb") # 200 bytes = 200 keys
sampleRegex = "^[a-zA-Z0-9_, .-]*$"

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
        
if __name__ == "__main__":
    #print(x_or_chipers())
    guess_word1(" for people around the world with ")
    print_list()

# next -->  , rule

# Word list
# Whe  61, As, 128, this 142, " has a" internet 70

# " this"  142  guess " the "
# "has a"  127  guess " the "
# "freed"  82   guess " the " 
# "ence"   22   guess " the "

# " of,"  142   guess " of "
# " net"  52    guess " of "
# "rude"  46    guess " of "
# "oelt"  12    guess " of "

# "them"  61    guess "them"

# "hate" 127    guess " to "    -->  " to a "
# "end"  22     guess " to "

# " as " 143    guess  " as "

# " in," 142    guess  " in "
# "icur" 109    guess  " in "
# "inhi" 106    guess  " in "
# "eksb" 99     guess  " in "
# "foc " 82     guess  " in "
# "eft " 49     guess  " in "
# "rsle" 46     guess  " in "
# "ese "  22    guess  " in "
# "ocdt" 12     guess  " in "

# " is,"        guess  " is "

# "rule"        guess  " on "

# "ficed"       guess " one "

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




