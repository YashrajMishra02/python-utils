import utils

# Test 1: prime sieve question
number = int(input("Enter the number and find all prime number till it: "))

print(f"The prime numbers are: {utils.prime_sieve(number)}")

# Test 2: caesar cipher
text = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt' or 'decrypt': ")

print(f"The result is: {utils.caesar_cipher(text, shift, mode)}")

# Test 3: Printing fibonacci series
index = int(input("Enter the index till which you want to see the fibonnaci series: "))
utils.fibGen(index)

# Test 4: Flatten list using for loop 
mylist = [[1,2,3],[4,5,6],[7,8,9]]
utils.fltUsgFor(mylist)

# Test 4: Flatten list using nested list comprehension
m = [[1,2,3],[4,5,6],[7,8,9]]
print(utils.fltUsgComp(m))

# Test 5: Fibonnaci generator recursively
number = int(input("Enter the index of which you want to see the fibonnaci number: "))
print(f"The fibnacci index of {number} is {utils.fibgen(number)}")
