num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
print(hcf(num1,num2))

# def hcf(num1,num2):
#     if num1==0 or num2==0:
#         return num1+num2
#     if num1==num2:
#         return num1
#     if num1<num2:
#         return hcf(num1,num2-num1)
#     else:
#         return hcf(num1-num2,num2)



