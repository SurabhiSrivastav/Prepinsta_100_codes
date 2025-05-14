num=int(input('Enter a number: '))
power= int(input('Enter power to raise: '))
print(num**power)

# alternate
power_num = pow(num,power)
print(power_num)

# alterenate
output=1
for i in range(power):
    output*=num
print(output)

# alternate
def power_num(num,power):
    if power==0:
        return 1
    return num*power_num(num,power-1)
print(power_num(num,power))