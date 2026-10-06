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
