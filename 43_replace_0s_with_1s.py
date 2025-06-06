num=int(input('Enter a num: '))
st=str(num)
l=[]
for s in st:
    if s=='0':
        l.append('1')
    else:
        l.append(s)
# print(l)
new_st=""
for i in l:
    new_st+=i
print(int(new_st))

# alternate
new_str=""
for s in st:
    if s=='0':
        new_str+='1'
    else:
        new_str+=s
print(int(new_str))

# alternate
new_num=0
# l=[]
if num==0:
    new_num=1
while num>0:
    rem = num % 10
    if rem == 0:
        rem=1
    num//=10
    new_num= new_num*10+rem
# print(new_num)
num=0
while new_num>0:
    r=new_num%10
    num=num*10+r #102->211--0+1 =1, 21--1*10+1=11, 2--11*10+2 = 112
    new_num//=10
print(num)