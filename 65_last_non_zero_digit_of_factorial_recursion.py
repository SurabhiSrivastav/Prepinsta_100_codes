n=int(input('Enter a number: '))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

fact=factorial(n)

def non_zero_digit(fact):
    rem=fact%10
    if rem!=0:
        return rem
    return non_zero_digit(fact//10)

print("Last non-zero digit of factorial:",non_zero_digit(fact))


# while fact%10==0:
#     fact//=10
# print(fact%10)