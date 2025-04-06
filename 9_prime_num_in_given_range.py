from sympy.codegen.ast import continue_

start= int(input('Enter start number: '))
end = int(input('Enter end number: '))
primes=[]
for i in range(start,end+1):
    flag=0
    if i <2:
        continue
    if i==2:
        primes.append(2)
        continue
    for x in range(2,i):
        if i%x==0:
            flag=1
            break
    if flag==0:
        primes.append(i)
print("Prime number list",primes)

# 2 optimized code
primes=[]
for num in range(start,end+1):
    flag=0
    if num <2:
        flag=1
    elif num==2:
        flag=0
    elif num%2==0:
        continue
    iter=2
    while iter < int(num/2):
        if num%iter==0:
            flag=1
            break
        iter+=1
    if flag==0:
        primes.append(num)
print('Prime list: ',primes)

# optimized using sqrt(num)
primes=[]
for num in range(start, end+1):
    flag=0
    if num<2:
        flag=1
    if num==2 or num==3:
        primes.append(num)
    if num%2==0:
        continue
    if num%3==0:
        continue
    iter =2
    while iter<int(pow(num,0.5)):
        if num% iter==0:
            flag=1
            break
        iter+=1
    if flag==0:
        primes.append(num)
print(primes)

# optimized
primes =[]
for num in range(start, end+1):
    flag=0
    if num<2:
        continue
    if num ==2 or num==3:
        primes.append(num)

    if num%2==0:
        continue
    if num%3==0:
        continue
    iter =3
    while iter <= int(pow(num,0.5)):
        if num%iter==0:
            flag=1
            break
        iter+=2
    if flag==0:
        primes.append(num)
print('prime: ',primes)
