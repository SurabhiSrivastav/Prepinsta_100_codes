num1= int(input('Enter first number: '))
num2= int(input('Enter second number: '))

lcm = 1
for i in range(max(num1, num2), 1+(num1*num2)):
    if i%num1==i%num2==0:
        lcm =i
        break
print(lcm)

def get_hcf(num1, num2):
    if num1==0 or num2==0:
        return num1+num2
    if num1==num2:
        return num1
    if num1>num2:
        return get_hcf(num1-num2,num2)
    else:
        return get_hcf(num1, num2-num1)
hcf=get_hcf(num1,num2)
lcm=(num1*num2)//hcf
print(lcm)