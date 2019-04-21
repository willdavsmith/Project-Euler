# finds the sum of even-valued terms of the
# fibonacci sequence below 4,000,000
def p2(n):
    return sum(filter(lambda x: x%2==0, gen_fib(n)))

# generates a list of fibonacci numbers up to
# and excluding n
def gen_fib(n):
    fib_list = [1,2]
    i = 2
    while fib_list[len(fib_list)-1] < n:
        fib_list.append(fib_list[i-2]+fib_list[i-1])
        i+=1
    return fib_list[:len(fib_list)-1]

print(p2(4000000))
