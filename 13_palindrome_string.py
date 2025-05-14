string= str(input('Enter a string: '))
j =-1
flag=0
for char in string:
    if char!=string[j]:
        flag=1
        break
    j=j-1

print(string + " is ", end="")
print("Not Palindrome") if flag else print("Palindrome")

# alternate
def check_pal(str):
    mid= int(len(str)/2)
    for i in range(0,mid):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
s=str(input("Enter a string: "))
print("Palindrome") if check_pal(s) else print("Not Palindrome")