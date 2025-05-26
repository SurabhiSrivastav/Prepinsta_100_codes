import math
num1= int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

def divisor(n,i=1):
    factors=[]
    i=1
    while i<=math.sqrt(n):
        if n%i==0:
            if n/i==i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
        i=i+1
    return sum(factors)-n #finding sum of factors, since factor included number itself therefore subtracting n
sum1=divisor(num1)
sum2=divisor(num2)

ratio1=sum1/num1
ratio2=sum2/num2

if ratio1==ratio2:
    print('Numbers are friendly pair')
else:
    print('Numbers are not friendly pair')