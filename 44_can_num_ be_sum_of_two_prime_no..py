from sympy.codegen.ast import continue_
n=int(input('Enter a number: '))
prime_list=[]
for num in range(2,n+1):
    flag = 0
    for iter in range(2, int(pow(num,0.5))+1):
        if num%iter==0:
            flag=1
            break
    if flag==0:
        prime_list.append(num)
print(prime_list)


j=len(prime_list)-1
for i in range(len(prime_list)):
    while i<j:
        sum=prime_list[i]+prime_list[j]
        if sum>n:
            j -= 1
        elif sum<n:
            i+=1
        elif sum==n:
            print(prime_list[i],',',prime_list[j])
            i+=1
            j-=1


