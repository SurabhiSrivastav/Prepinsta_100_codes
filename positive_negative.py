num=int(input("Enter a positive or negative number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")  
else:
    print("number is zero")


## alternate way using nested if-else
if num>=0:
    if num==0:
        print("num is zero")
    else:
        print("num is positive")
else:
    print("num is negative")     

# alternate way using ternary operator
print("Positive" if num>=0 else "Negative")

