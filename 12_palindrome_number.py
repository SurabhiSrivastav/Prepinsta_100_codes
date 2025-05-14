num=int(input('Enter a number: '))
rev=0
def reverse(num,rev):
    if num==0:
        return rev
    rem=num%10
    rev=(rev*10)+rem
    return reverse(num//10,rev)

reverse_num=reverse(num,rev)
print("Pallindrome") if reverse_num==num else print("Not a Pallindrome")

# alternate using string slicing

reverse_num=int(str(num)[::-1])
if num==reverse_num:
    print("Pallindrome")
else:
    print("Not Pallindrome")