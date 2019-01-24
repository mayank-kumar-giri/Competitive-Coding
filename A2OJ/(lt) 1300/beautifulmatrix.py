matrix = []
x1 = 0
y1 = 0
for i in range(5):
    temp = list(input().split())
    matrix.append(temp)
    if '1' in temp:
        x1 = i + 1
        y1 = temp.index('1') + 1
moves = abs(3-x1) + abs(3-y1)
print(moves)