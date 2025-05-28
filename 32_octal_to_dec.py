num=int(input('Enter an octal number: '))

decimal_num=0
base=1

while num!=0:
    rem=num%10
    decimal_num+=rem*base
    num=num//10
    base=base*8
print(decimal_num)