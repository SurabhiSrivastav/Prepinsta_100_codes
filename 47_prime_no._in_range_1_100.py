primes=[]
for num in range(1,101):
    flag=0
    if num<2:
        flag=1
    if num==2:
        primes.append(num)
    if num%2==0:
        continue
    iter=3
    while iter<=int(pow(num,0.5)):
        if num%iter==0:
            flag=1
            break
        iter+=1
    if flag==0:
        primes.append(num)

print('Prime numbers in range 1 to 100: ',primes)

# alternate
def isPrime(num):
    if num<2:
        return False
    # if num==2:
    #     return True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

prime_no=[]
for num in range(1,101):
    if isPrime(num):
        prime_no.append(num)
print('Prime list till 100: ',prime_no)