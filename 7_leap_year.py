num = int(input("Enter value of any year"))
if num%4==0 and num%100!=0:
    if num%400==0 :
        print(num, "is leap year")
    else:
        print(num, "is not a leap year")