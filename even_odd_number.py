num = int(input("Enter a number: "))
if num%2==0:
    print("number is even")
else:
    print("number is odd")

#alternate way using ternary operator
print("Even" if num%2==0 else "Odd") ##other way to write it as:- print("even")if num%2==0 else print("odd")

#alternate way using bitwise operator
def isEven(num):
    # print(num&1)
    # print(not num&1) boolean value
    return not num&1   #bitwise & will give 1 if num is odd and 0 if num is even
if __name__ =="__main__":
    if isEven(num):
        print("Even number")
    else:
        print("Odd number")

