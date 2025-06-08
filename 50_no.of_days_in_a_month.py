month=str(input('Enter a month(in "Jan/January/1" format): ')).lower()
month_dict={
    'j': ['jan','january','1'],
    'f': ['feb', 'february', '2'],
    'mr': ['mar', 'march', '3'],
    'a': ['apr', 'april', '4'],
    'm': ['may', '5'],
    'ju': ['jun', 'june', '6'],
    'jl': ['jul', 'july', '7'],
    'au': ['aug','august', '8'],
    's': ['sep', 'september', '9'],
    'o': ['oct', 'october', '10'],
    'n': ['nov', 'november', '11'],
    'd': ['dec', 'december', '12']
}

found = False
for key, values in month_dict.items():
    if month in values:
        m=key
        found=True

if m == 'j' or m == 'j' or m == 'mr' or m == 'm' or  m == 'jl' or m == 'au' or m == 'o' or m == 'd':
    print('number of days in this month is 31')
elif m=='a' or m == 'ju' or m == 's' or m == 'n':
    print('number of days in this month is 30')
elif m=='f':
    year= int(input('Enter current year: '))
    if year%400==0 or year%100!=0 and year%4==0:
        print("As it's leap year, so no. of days is 29")
    else:
        print("Not a leap year, therefore no. of days is 28")
else:
    print('Invalid input')