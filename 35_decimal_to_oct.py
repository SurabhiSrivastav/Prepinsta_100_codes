num=int(input('Enter a decimal number: '))
oct=0
i=1

while num!=0:
    rem=num%8
    num=num//8
    oct+=rem*i
    i*=10
print(oct)