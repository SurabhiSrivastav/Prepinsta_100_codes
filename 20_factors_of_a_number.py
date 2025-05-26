num=int(input('Enter a number: '))
for i in range(num):
    if num%(i+1)==0:
        print(i+1,end=" ")

# alternate

import math
def factors_number(num):
    factors=[]
    i=1
    while i<= math.sqrt(num):
        if (num%i==0):
            if(num/i==i):
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(num/i))
        i = i+1
    return sorted(factors)
print(factors_number(num))

