num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))
num3= int(input("Enter third number:"))

if num1>=num2 and num1>=num3:
    print(num1, "is greatest")
elif num2>=num1 and num2>=num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")

#using nested if-else
if num1>=num2:
    if num1>=num3:
        print(num1, "is greater")
elif num2>=num3:
    print(num2, "is greater")
else:
    print(num3, "is greater")

#using ternary operator
max= num1 if num1>num2 else num2
ans = num3 if num3>max else max
print(ans)