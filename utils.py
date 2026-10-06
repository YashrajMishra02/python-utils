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
