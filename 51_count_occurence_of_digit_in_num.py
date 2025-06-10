num = int(input('Enter a number: '))
digit= int(input('Enter a digit to look for: '))
cnt = 0
while num!=0:
    rem=num%10
    if digit==rem:
        cnt+=1
    num=num//10

if cnt >0:
    print(f"{digit} occurs {cnt} time in given number")
else:
    print("digit isn't found in given number")

