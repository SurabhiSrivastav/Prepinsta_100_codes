st=str(input('Enter a string: '))
stl=list(st)
unique_perm=set()
l=0
r=len(stl)-1

def str_permutations(stl,l,r,unique_perm):
    if l==r:
        unique_perm.add(''.join(stl))
    else:
        for i in range(l,r+1):
            stl[l],stl[i] = stl[i], stl[l] #swap
            str_permutations(stl,l+1,r,unique_perm) #recur
            stl[l],stl[i]=stl[i],stl[l] #backtrack

str_permutations(stl,l,r,unique_perm)
print(sorted(unique_perm))
