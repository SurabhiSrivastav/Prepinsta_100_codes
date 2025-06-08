num=int(input('Enter any integer number: '))

count_num=0
while num!=0:
    num=num//10
    count_num+=1
print(count_num)

# alternate method using formula
n=int(input('Enter number: '))
import math
digit = math.floor(math.log10(n)+1)
print(digit)

