n=int(input('Enter a number: '))
def Fibonacci(n):
    if n<2:
        return n
    fs=[0,1]
    for i in range(1,n):
        fs.append(fs[i]+fs[i-1])
    return fs[n]
print(Fibonacci(n-1))

# alternate
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(n-1))