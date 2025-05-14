start=int(input("Enter first number: "))
end=int(input("Enter second number: "))
for n in range(start, end+1):
    order= len(str(n))
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if n==sum:
        print("armstrong in this range is: ",n)

# alternate
import math
def armstrong_in_range(val):
    sum=0
    arr = [int(d) for d in str(val)]
    for i in range(0,len(arr)):
        sum+=math.pow(arr[i],len(arr))
    if sum==val:
        print(str(val)+ ", ", end="")

print("Armstrong num in this range is: ")
for i in range(start,end+1):
    armstrong_in_range(i)
