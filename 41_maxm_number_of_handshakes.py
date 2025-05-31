"""since,no people should handshake twice, it's to be unique therefore, total no. of handshakes would be:
(n-1)+(n-2)+(n-3)+.......3+2+1+0, which is basically sum of the first n-1 numbers. Sum can be rewritten as pairs
where each pair sums to n-1, and there are total n/2 pairs, therefore formula= n(n-1)/2"""

num=int(input('Enter number of people in the room: '))
num_of_handshakes=int(num*(num-1)/2)
print(f'Total no. of unique handshakes: {num_of_handshakes}')