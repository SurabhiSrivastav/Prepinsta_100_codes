num = int(input('Enter a number: '))
rev=0
while num!=0:
    rem= int(num%10)
    rev = (rev*10)+rem
    num=num//10
print("Reverse of given number is: ", rev)

# Alternate using recursion
def reverse(num,rev):
    if num==0:
        return rev
    rem=int(num%10)
    rev= (rev*10)+rem
    return reverse(num//10,rev)
print("Reverse of number is: ", reverse(num,rev))