sum=0
num=int(input("enter a number to print sum for: "))
for i in range(num+1):
    sum+=i
print(sum)    

#alternate way using formula of sum of nth term
sum = int(num*(num+1)/2)
print(sum)

# using recursion
def findSum(num):
    if num==0 or num==1:
        return num
    else:
        return num + findSum(num-1)
print(findSum(num))