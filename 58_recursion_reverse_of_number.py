n=int(input('Enter a number to be reversed: '))
rev=0
def reverse_num(n,rev):
    if n==0:
        return rev
    rem=n%10
    rev= (rev*10)+rem
    return reverse_num(n//10,rev)
print('Reverse of number: ', reverse_num(n,rev))

