a= int(input('Enter the value of base number: '))
b= int(input('Enter value of power: '))

def power_recursion(a,b):
    if b==0:
        return 1
    else:
        return a * power_recursion(a,b-1)

print(power_recursion(a,b))