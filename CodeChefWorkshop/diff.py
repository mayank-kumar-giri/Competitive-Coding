t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ll = 0
    if k<=int(n/2):
        ll = k
    else:
        ll = n-k
    ans = sum(arr[ll:]) - sum(arr[:ll])
    print(ans)