t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for j in a:
        if j!=1:
            c+=1
    if c<=k:
        print("YES")
    else:
        print("NO")