n=int(input('Enter a number: '))
factorial=1
if n<0:
    print('Factorial not possible')
elif n==0:
    print('factorial of 0 is 1')
else:
    for i in range(1, n+1):
        factorial=factorial*i
    print("The factorial of", n, "is", factorial)


#alternate
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))