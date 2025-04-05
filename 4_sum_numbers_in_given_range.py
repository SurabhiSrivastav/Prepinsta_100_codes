sum=0
start=int(input("Enter start number"))
end=int(input("Enter end number"))
for i in range(start, end+1):
    sum+=i
print(sum)

#alternate using formula
sum= int(end*(end+1)/2)-int(start*(start+1)/2)+start
print(sum)

#alternate using recursion
def sum_num_in_given_range(sum,start,end):
    if start>end:
        return sum
    # print("sum is", sum)
    return start+sum_num_in_given_range(sum,start+1,end)
sum=0
print(sum_num_in_given_range(sum,start,end))