num= int(input('Enter a binary number: '))
# 10-->2, 0110-->6
decimal_num=0
base=1
while num!=0:
    rem=num%10
    decimal_num+=base*rem
    num=num//10
    base=base*2
print(decimal_num)

