num=int(input('Enter a number: '))
for i in range(num):
    if num%(i+1)==0:
        print(i+1,end=" ")
    i+=1

# alternate

import math
def factors_number(num):
    i=1
    while i<= math.sqrt(num):
        if (num%i==0):
            if(num/i==i):
                print(i, end=" ")
            else:
                print(i, int(num / i), end=" ")
        i = i+1
print(factors_number(num))

