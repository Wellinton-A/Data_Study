def fibonacciIterative(n):
    fib = [0,1]
    while n > 1:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
        n -= 1
    return fib[len(fib)-1]

print(fibonacciIterative(20))  

def fibonacciRecursive(n):
    if n < 2 :
        return n
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    
print(fibonacciRecursive(40))