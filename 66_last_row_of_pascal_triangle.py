# 1
# 11
# 121
# 1331
# 14641-->ncr=ncr-1*(n-r+1)/r

n=int(input('Enter a number: '))

def pascal_row(n, i, prev_row=None):
    if prev_row is None:
        prev_row = [1]
    if i>n:
        return prev_row
    curr_row=[1]
    for j in range(len(prev_row)-1):
        curr_row.append(prev_row[j]+prev_row[j+1])
    curr_row.append(1)

    return pascal_row(n,i+1,curr_row)

print(pascal_row(n,1))

