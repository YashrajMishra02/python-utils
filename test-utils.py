import utils

# Test 1: prime sieve question
number = int(input("Enter the number and find all prime number till it: "))

print(f"The prime numbers are: {utils.prime_sieve(number)}")

# Test 2: caesar cipher
text = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt' or 'decrypt': ")

print(f"The result is: {utils.caesar_cipher(text, shift, mode)}")
