import math

a=int(input('Enter value for a as per quadratic equation(a*x^2 + bx +c): '))
b=int(input('Enter value for b as per quadratic equation(a*x^2 + bx +c): '))
c=int(input('Enter value for c as per quadratic equation(a*x^2 + bx +c): '))

def quad_roots(a,b,c):
    if a == 0:
        print("Invalid")
        return -1

d= (b**2)-(4*a*c)
sqrt_d= math.sqrt(abs(d))

if d>0:
    print("Roots are real and different")
    print((-b+sqrt_d)/(2*a))
    print((-b-sqrt_d)/(2*a))

elif d==0:
    print("Roots are real and equal")
    print(-b/(2*a))

else:
    print("Roots are imaginary")
    print(-b / (2 * a), "+i", sqrt_d)
    print(-b / (2 * a), "-i",sqrt_d)
