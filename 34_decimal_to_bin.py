num= int(input('Enter a decimal number: '))
bin=0
i=1

while num!=0:
    rem= num%2
    num=num//2
    bin+=rem*i
    i*=10
print(bin)