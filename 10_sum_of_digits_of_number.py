num = int(input('Enter a number: '))
sum=0
while num!=0:
    rem = int(num%10)
    sum+=rem
    num=num/10
print(sum)

# Alternate method using recursion
def find_sum(num, sum):
    if num==0:
        return sum
    digit = int(num%10)
    sum+=digit
    return find_sum(num/10, sum)
print(find_sum(num,sum))

# more optimized

def find_sum_num(num):
    if num==0:
        return 0
    return int(num%10)+find_sum_num(num/10)
print(find_sum_num(num))