 # abundant number is number, sum of divisor of which is greater than the number itself
num=int(input('Enter a number: '))
divisor_sum=0
for i in range(1,num):
     if num%i==0:
         divisor_sum+=i
print(divisor_sum)
if divisor_sum>num:
    print('It\'s abundant number')
else:
    print('It\'s not abundant number')
