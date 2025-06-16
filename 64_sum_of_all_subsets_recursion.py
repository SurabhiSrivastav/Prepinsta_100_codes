def subset_sum(arr,l,r,sum=0,result=None):
    if result is None:
        return []
    if l>r:
        result.append(sum)
        return result
    subset_sum(arr,l+1,r,sum+arr[l],result) #Include current element
    subset_sum(arr,l+1,r,sum,result) #Exclude current element
    return result


inp_arr= input('Enter numbers in array separated by comma: ')
arr= list(map(int,inp_arr.split(",")))
l=0
r=len(arr)-1
print(subset_sum(arr,l,r))

