num= int(input('Enter a number: '))

def prime_num(num,iter=2):
    if num<2:
        return False
    elif num==iter:
        return True
    elif num%iter==0:
        return False
    else:
        return prime_num(num,iter+1)
if prime_num(num):
    print('Prime number')
else:
    print('Non Prime')
