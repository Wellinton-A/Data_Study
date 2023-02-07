
# cache = dict()

# def memoization(n):
#     if n in cache:
#         return cache[n]
#     else:
#         print('I\'ve been here')
#         cache[n] = n + 80
#         return n + 80
    
# print(memoization(5))
# print(memoization(5))
# print(memoization(6))
# print(memoization(6))


calculations = 0

def fibonacci(n):
    global calculations
    calculations += 1
    if n < 2 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(20))

print(f'we did: {calculations} calculations')

def fibonacciIter(n):
    fib = [0, 1]
    if n < 2 :
        return n
    while n > 1:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
        n-=1
    return fib[len(fib)- 1]

print(fibonacciIter(50))

calculations2 = 0
def fibonacciCache(n, cache = {}):
    global calculations2
    calculations2 += 1
    if n in cache:
        return cache[n]
    else:
        if n < 2 :
            return n
        else:
            cache[n] = fibonacciCache(n-1) + fibonacciCache(n-2)
            return cache[n]

print(fibonacciCache(500))
print(f'we did: {calculations2} calculations')