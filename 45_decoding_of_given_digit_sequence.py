num=str(input('Enter a digit sequence: '))

def decoding_digit(s):
    if not s or s[0]=='0':
        return 0
    prev,curr=1,1 #empty string has 1 way
    print(len(s))
    for i in range(1,len(s)):
        temp=0
        print('s[i]',s[i])
        if s[i]!='0':
            temp+=curr
            print('temp', temp)
        two_digit=int(s[i-1:i+1])
        print('two_digit', two_digit)
        if 10<=two_digit<=26:
            temp+=prev
            print('temp', temp)
        prev,curr=curr,temp
        print('prev', prev)
        print('curr', curr)
    return curr

print(decoding_digit(num))