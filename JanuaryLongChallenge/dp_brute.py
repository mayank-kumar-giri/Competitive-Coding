n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
d = {}
c=0
for i in range(n):
    for j in range(m):
        f=0
        try:
            if d[a[i]+b[j]]==True:
                f=1
        except:
            f=0
        if not f:
            # print(c,[i,j])
            ans.append([i,j])
            d[a[i] + b[j]] = True
            c+=1
        if c >= (n + m - 1):
            break
    if c>=(n+m-1):
        break
for i in ans:
    print(i[0],i[1])