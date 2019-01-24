t = int(input())
for i in range(t):
    n,p = map(int, input().split())
    if n==1 or n==2:
        print(p**3)
        continue
    maximum = n%(int(n/2)+1)
    k = p - maximum
    y = p - n
    ans = (k**2)+(k*y)+(y**2)
    print(ans)