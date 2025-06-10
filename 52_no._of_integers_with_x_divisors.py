num= int(input('Enter a number: '))
divisor=int(input('Enter a divisor: '))
cnt_total_divisor=0
for i in range(1, num+1): #-->1,5 -->2divisor-->2,3,5-->ans=3
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==divisor:
        # print(j)
        cnt_total_divisor+=1
print(cnt_total_divisor)
