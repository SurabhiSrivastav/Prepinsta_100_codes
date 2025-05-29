""" Permutations (order matters): nPr = n! / (n - r)!
Combinations (order doesn't matter): nCr = n! / (r! * (n - r)!) """

n= int(input('Enter number of students: '))
r= int(input('Enter number of seats available in class: '))

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

permutation= factorial(n)//factorial(n-r)
print(f'Permutations in which n people can occupy r seats in a classroom: {permutation}')