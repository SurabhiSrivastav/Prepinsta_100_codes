num= int(input('Enter a number: '))

def num_to_words_100(num):
    ones= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if num<20:
        return ones[num]
    else:
        return tens[num // 10] + ' ' + (ones[num%10] if num%10!=0 else '')

def num_to_words_all(n):
    st = ''

    if n ==0:
        return 'zero'
    if n >= 100000 :
        st += str(num_to_words_100((n // 100000))) + ' lakh '
        n%=100000
    if n >= 1000 :
        st += str(num_to_words_100((n // 1000))) + ' thousand '
        n%=1000
    if n >= 100 :
        st += str(num_to_words_100((n // 100))) + ' hundred '
        n%=100
    if n > 0:
        st += num_to_words_100(n)
    return st

print(num_to_words_all(num))