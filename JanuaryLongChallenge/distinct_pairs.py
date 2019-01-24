n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
da = {}
db = {}
for i in range(n):
    f = 0
    try:
        if da[a[i]] >= 0:
            f = 1
    except:
        f = 0
    if not f:
        da[a[i]] = i
for i in range(m):
    f = 0
    try:
        if db[b[i]] >= 0:
            f = 1
    except:
        f = 0
    if not f:
        db[b[i]] = i
a = sorted(a)
b = sorted(b)
prev = a[0]
c = 0

for i in range(n):
    if i!=0 and a[i]==prev:
        continue
    for j in range(m):
        if j==0 or (j!=0 and b[j]!=prevb):
            ans.append([da[a[i]],db[b[j]]])
            c+=1
        prevb = b[j]
        if c>=n+m-1:
            break
    if c>=n+m-1:
        break
    prev = a[i]

for i in ans:
    print(i[0],i[1])