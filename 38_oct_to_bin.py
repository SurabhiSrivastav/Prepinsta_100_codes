# for oct to bin conversion will first convert oct to dec and dec to bin
num= int(input('Enter an octal number: '))
dec,bin=0,0
o_base,d_base=1,1

while num!=0:
    rem=num%10
    num=num//10
    dec+=rem*o_base
    o_base*=8

print(dec)

dec_rem=dec
while dec_rem!=0:
    rem=dec_rem%2
    dec_rem=dec_rem//2
    bin+=rem*d_base
    d_base*=10
print(bin)
