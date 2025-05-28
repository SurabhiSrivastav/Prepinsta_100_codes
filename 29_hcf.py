num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
# hcf and gcd are same
hcf=1
for i in range(1, min(num1, num2)):
    if num1%i==0 and num2%i==0:
        hcf=i
print(hcf)

# alternate
def hcf_num(num1, num2):
    if num1==0 or num2==0:
        return num1+num2
    if num1==num2:
        return num1
    if num1>num2:
        return hcf_num(num1-num2, num2)
    else:
        return hcf_num(num1, num2-num1)

print(hcf_num(num1,num2))

# alternate
a= int(input('Enter first number: '))
b= int(input('Enter second number: '))
def get_hcf(a,b):
    if b==0:
        return a
    else:
        return get_hcf(b, a%b)
print(get_hcf(a,b))

# it can also be written in one line:- return b==0 and a or get_hcf(b,a%b)