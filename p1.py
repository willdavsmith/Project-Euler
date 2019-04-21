# returns the sum of all multiples of 3 or 5
# less than n
def p1(n):
    return sum(filter(lambda x: x%3==0 or x%5==0, list(range(1,n))))

print(p1(1000))
