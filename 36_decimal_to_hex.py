num=int(input('Enter a decimal number: '))
hex=''
hex_to_dec={0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

while num!=0: #2545
    rem=num%16 #2545%16= 1 --> 15-->9
    num=num//16 #159-->9-->0
    hex+=str(hex_to_dec[rem])
print(hex[::-1]) #start:stop:step---> step +ve slicing moves fwd, step -ve slicing moves bwd

# alternative to reverse
# final_hex=''.join(reversed(hex))
# print(final_hex)