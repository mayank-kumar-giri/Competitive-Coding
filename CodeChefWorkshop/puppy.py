t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    if k>n:
        print(n)
        continue
    ans = 0
    # maxi = 0
    for j in range(1,k+1):
        temp = n%j
        if ans<=temp:
            ans = temp
            # maxi = j
            # print(j,ans)
    print(ans)