# perfect number is a number, sum of divisors of which is equal to the number itself
num=int(input('Enter a number: '))
sum=0
for i in range(1, num+1):
    if num%i==0 and num!=i:
        print(i)
        sum+=i
print(sum)
if sum==num:
    print('It\'s a perfect number')

