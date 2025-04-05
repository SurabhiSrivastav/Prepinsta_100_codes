num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
if num1>num2:
    print(num1, "is greater")
else:
    print(num2, "is greater")


#using ternary operator
print(num1 if num1>num2 else num2)

#using max function
maxm = max(num1, num2)
print("greatest number is:",maxm)

