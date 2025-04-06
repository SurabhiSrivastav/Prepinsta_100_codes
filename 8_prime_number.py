num = int(input('Enter a number: '))
flag=0
if num<2:
    flag=1
else:
    for i in range(2, num):
        if num%i==0:
            flag=1
            break
if flag==1:
    print('Not prime')
else:
    print('Prime')

#2. Optimized code i.e. if can be factorized in n/2 iterations then too, it's not prime
num = int(input('Enter a number: '))
flag=0
if num<2:
    flag=1
else:
    for i in range(2, int((num/2)+1)):
        if num%i==0:
            flag=1
            break
if flag==1:
    print('Not prime')
else:
    print('Prime')

#3. Further optimized i.e. if num is divisible in b/w range 2, sqrt(num), then too it's not prime
num = int(input('Enter a number: '))
flag=0
if num<2:
    flag=1
else:
    for i in range(2, int(pow(num,0.5)+1)):
        if num%i==0:
            flag=1
            break
if flag==1:
    print('Not prime')
else:
    print('Prime')

# Since, 2 is only even prime no. rest all even no. are non-prime, so will skip all even n. from range and hence reduce iteration by 50%
num = int(input('Enter a number: '))
flag=0
if num<2:
    flag=1
elif num==2:
    flag=0
elif num%2==0:
    flag=1
else:
    for i in range(3, int(pow(num,0.5)+1), 2):
        if num%i==0:
            flag=1
            break

if flag==1:
    print('Non prime')
else:
    print('Prime')

# Recursion based approach

def check_prime_num(num, iter=2):
    if num<2:
        return False
    elif num==iter:
        return True
    elif num%iter==0:
        return False
    else:
        return check_prime_num(num,iter+1)
if check_prime_num(num)== True:
    print('Prime')
else:
    print('Non Prime')


