inp_arr= input('Enter numbers seperated by comma: ')
arr= list(map(int,inp_arr.split(",")))
l=len(arr)

def smallest_rec(arr, l):
    if l==1:
        return arr[0]
    return min(arr[l-1],smallest_rec(arr,l-1))
print(smallest_rec(arr,l))