t= int(input())
for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1]<=k:
        print(sum(a))
    elif a[-2]<=k:
        print(sum(a))
    else:
        j = 0
        for l in a:
            if l>k:
                break
            j+=1
        lk = sum(a[:j])
        mc = a[-1]-(a[-2]-k)
        rc = k*(n-j-1)
        print(lk,mc,rc)
        summ = lk+mc+rc
        print(summ)