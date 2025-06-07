from math import pi
r=float(input('Enter radius of circle: '))
d= float(input('Enter diameter of circle: '))

area_r= pi*r*r
area_d= (pi*d*d)/4 #pi*(d/2)*(d/2)
if r:
    print(f"area of circle using radius: {area_r:.2f}")
elif d:
    print(f"area of circle using diameter: {area_d:.2f}")