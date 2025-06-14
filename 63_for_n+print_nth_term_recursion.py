n=int(input('Enter a number: '))
# F(N)= (1) +(2*3) + (4*5*6) …

def nth_term(calculated, current,n):
    cur=1
    if current==n+1:
        return 0
    for i in range(calculated, calculated+current):
        cur*=i
    return cur+ nth_term(calculated+current,current+1,n)

print(nth_term(1,1,n))