num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

def lcm(a,b):
    return (a*b)//hcf(a,b)

print(lcm(num1,num2))