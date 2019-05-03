t = int(input())
for i in range(t):
    n,d = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans = [0]*n

    for j in range(1,n):
        ans[j] = ans[j-1]
        if (arr[j]-arr[j-1])<d:
            if j>=2:
                ans[j] = max(ans[j],ans[j-2] + arr[j] + arr[j-1])
            else:
                ans[j] = max(ans[j],arr[j] + arr[j-1])

    print(ans[n-1])