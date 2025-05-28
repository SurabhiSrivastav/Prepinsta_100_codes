num=input('Enter a hexadecimal number: ').upper()
hex_to_dec={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
hex_len=len(num)
# print(hex_len)
dec_num=0

for ch in num:
    hex_len=hex_len-1
    # print(hex_len)
    # print(hex_to_dec[ch])
    dec_num+= hex_to_dec[ch]*(16**hex_len)

print(dec_num)

""" Ex :
9 = 9 * (16 ^ 0) = 9
C = 12 * (16 ^ 1) = 192
C9= 201
"""