# Day 1 code: Prime sieve question: Find all prime numbers till a given number using the Sieve of Eratosthenes algorithm

def prime_sieve(number):
    s = set()
    for i in range(2, number):
        for j in range(2, i+1):
            if(i==j):
                s.add(i)
                continue
            elif(i%j!=0):
                continue
            elif(i%j==0):
                break
    return s

# Day 2 code : caesar cipher (encryption and decryption) i.e. shift each letter by a fixed number of positions in the alphabet
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # If decrypting, we reverse the shift direction
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            # 65 is the ASCII value for 'A'
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            # 97 is the ASCII value for 'a'
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabet characters (spaces, punctuation) as they are
            result += char
            
    return result

# Day 3 code: Fibonnaci Series generator
def fibGen(index):
    zero = 0
    first = 1
    ans = 0
    print(zero, end=' ')
    print(first, end=' ')
    i = 2
    while i <= index:
        ans = zero + first
        print(ans, end=' ')
        zero = first
        first = ans
        i+=1

# Day 4 Code: Flatten Nested list using for loop
def fltUsgFor(m):
    flat = []
    
    for r in m:
        for e in r:
            flat.append(e)
    
    print(flat)

# Day 4 Code: Flatten Nested list using nested list comprehension
def fltUsgComp(m):
    flat = [e for row in m for e in row]
    return flat

# Day 5 Code: Fibonnaci generator recursively
def fibgen(num):
    if num == 0 or num == 1:
        return num
    smalloutput1 = fibgen(num - 1)
    smalloutput2 = fibgen(num - 2)
    return smalloutput1 + smalloutput2

# Day 6 Code: most_common () function to find the most common element in a list
from collections import Counter
def mst_com(lst):
    # return Counter(lst).most_common() # this will return the most common element in the list along with its count
    return Counter(lst).most_common(1)[0][0] # this will return the most common element in the list


# Day 7 Code: most_common () function to find the most common element in a string
def mst_str(string):
    # return Counter(string.split()).most_common() # this will return the most common element in the string along with its count
    return Counter(string.split()).most_common(1)[0][0] # this will return the most common element in the string