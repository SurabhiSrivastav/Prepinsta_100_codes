number=int(input("Enter a number: "))
sum=0
num=number
num_len = len(str(num))

for i in range(num_len):
    digit=int(num%10)
    num=num/10
    # print(num)
    sum+=pow(digit,num_len)
# print(sum)
# print(num)
if sum==number:
    print("Armstrong")
else:
    print("Not armstrong")




# alternate
number= int(input('Enter a no.: '))
sum=0
num=number
num_len= len(str(num))
def armstrong(num,sum,num_len):
    if num==0:
        return sum
    digit=num%10
    sum+=pow(digit,num_len)
    # print(num)
    return armstrong(num//10,sum,num_len)

if armstrong(num,sum,num_len)==number:
    print("armstrong")
else:
    print("not armstrong")