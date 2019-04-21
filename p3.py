import math

# returns the largest prime factor of n
def p3(n):
    product = 1
    i = 1
    while product < n:
        i = gen_prime(i)
        if n%i == 0:
            product *= i
    return i


# generates a prime number greater than n
# where n is a prime number
def gen_prime(n):
    k = n
    while True:
        k+=1
        if is_prime(k):
            return k

# checks if a number is prime by 
# trial division
def is_prime(n):
    for i in range(2,math.ceil(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

print(p3(317584931803))
