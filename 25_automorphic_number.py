# A number is automorphic if it's unit's place digit is same as the unit place digit of square of the number
num = int(input('Enter a number: '))

sq=num*num #alternate to calculate square of a num:- pow(number, 2)
if sq%10==num%10:
    print('Number is automorphic')
else:
    print('Number is not automorphic')

# Alternate using string endswith()

a= str(num)
num1 = num ** 2
b=str(num1)
if b.endswith(a):
    print('It\'s an automorphic number')
else:
    print('It\'s not automorphic')
