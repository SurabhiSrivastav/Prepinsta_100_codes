inp_arr= input('Enter numbers seperated by comma: ')
arr= list(map(int,inp_arr.split(",")))

l=len(arr)
def largest_rec(arr,l):
    if l==1:
        return arr[0]
    return max(arr[l-1], largest_rec(arr,l-1))
print(largest_rec(arr,l))