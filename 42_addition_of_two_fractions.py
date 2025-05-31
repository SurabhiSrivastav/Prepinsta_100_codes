num1, den1= map(int,list(input('Enter first numerator and deominator: ').split(" ")))
num2, den2= map(int,list(input('Enter second numerator and denominator: ').split(" ")))


new_num=num1*den2 + num2*den1
new_den=den1*den2

# finding gcd to simplify fraction val, as gcd of new numerator and denominator will reduce fraction value
gcd=1
for i in range(1, min(new_num,new_den)):
    if new_num%i==0 and new_den%i==0:
        gcd=i
# print(gcd)

res_num=new_num//gcd
res_den=new_den//gcd
# print(new_num,'/',new_den)
print("addition of two fraction is: ", res_num,'/', res_den)
