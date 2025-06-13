st=str(input('Enter yor string: '))

def string_len(st):
    if st=="":
        return 0
    return 1+string_len(st[1:])
print(string_len(st))