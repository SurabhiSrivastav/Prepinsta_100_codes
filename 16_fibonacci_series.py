num=int(input("Enter a num_range: "))
n1,n2=0,1
print(n1,n2, end=" ")
for i in range(2, num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")

# alternate
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
if num<=0:
    print("Enter a positive number: ")
else:
    print("\nFibonacci series:", end="")
for i in range(num):
    print(" ",fib(i), end="")