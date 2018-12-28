n = int(input())
v = []
x = y = z = 0
for i in range(n):
    temp = list(map(int, input().split()))
    x += temp[0]
    y += temp[1]
    z += temp[2]

if x==y==z==0:
    print("YES")
else:
    print("NO")