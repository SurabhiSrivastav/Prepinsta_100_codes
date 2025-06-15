inp_arr= input('Enter numbers in array seperated by comma: ')
arr= list(map(int,inp_arr.split(",")))
l=0
r=len(arr)-1

def subset_sum(arr:list,l,r,sum=0,result=[]):
    if result is None:
        return []
    if l>r:
        result.append(sum)
        return result
    subset_sum(arr,l+1,r,sum+arr[l],result)
    subset_sum(arr,l+1,r,sum,result)
    return result

print(subset_sum(arr,l,r))