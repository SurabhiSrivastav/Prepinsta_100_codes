# Harshad num is a num, sum of whose digits completely divides the num itself
num=int(input('Enter a number: '))
sum=0
n=num
while n!=0:
    digit=n%10
    sum+=digit
    n=n//10
# print(sum)
# print(num)
if num%sum==0:
    print('It\'s a Harshad number')
else:
    print('It\'s not Harshad number')