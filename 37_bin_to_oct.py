# for bin to oct conversion will first convert bin to dec and dec to oct
num= int(input('Enter a binary number: '))
dec=0
b_base=1
d_base=1
oct=0

while num!=0:
    rem=num%10
    num=num//10
    dec+= rem*b_base
    b_base*=2
print(dec)
num_dec=dec
while num_dec!=0:
    rem=num_dec%8
    num_dec=num_dec//8
    oct+= rem*d_base
    d_base*=10

print(oct)

