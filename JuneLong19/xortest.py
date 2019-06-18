n = 95

for i in range(1,1000):
    a = n ^ i
    print(bin(a),a)
    print(i,bin(n),n)
    print()