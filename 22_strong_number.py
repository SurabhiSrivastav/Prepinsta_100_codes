# strong number is a number, sum of factorial of whose digits is same as number.
n=int(input('Enter a no.: '))
# 145=1!+4!+5!
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=n
fact_sum=0
while num!=0:
    digit=int(num%10)
    # print("digit",digit)
    # print("facto",fact(digit))
    fact_sum+=fact(digit)
    num=num//10

# print(fact_sum)
# print(num)
# print(n)
if fact_sum == n:
    print(f'The number {n} is Strong number')
else:
    print('Given number is not Strong')
