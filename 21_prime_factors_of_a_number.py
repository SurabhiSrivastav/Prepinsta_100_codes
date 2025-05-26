num = int(input('Enter a number: '))
arr=[]
for i in range(2,num+1):
    while num%i==0:
        arr.append(i)
        num=num//i
print(arr)


# alternate
n = int(input('Enter a number: '))
def prime_factors(n,i=2):
    if n==1:
        return []
    if n%i==0:
        return [i]+ prime_factors(n//i,i)
    else:
        return prime_factors(n,i+1)

print(prime_factors(n))