x=int(input('Enter value for x coordinate: '))
y=int(input('Enter value for y coordinate: '))

# alternate way to take inputs
# x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))

if x==0 and y==0:
    print(f'point {x},{y} lies at origin')
elif x!=0 and y==0:
    print(f'point {x},{y} lies on x axis')
elif x==0 and y!=0:
    print(f'point {x},{y} lies on y axis')
elif x>0 and y>0:
    print(f'point {x},{y} lies in first quadrant')
elif x<0 and y>0:
    print(f'point {x},{y} lies in second quadrant')
elif x<0 and y<0:
    print(f'point {x},{y} lies third quadrant')
elif x>0 and y<0:
    print(f'point {x},{y} lies fourth quadrant')
