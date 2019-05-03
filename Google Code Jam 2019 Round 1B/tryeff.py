t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    count = 0

    for j in range(n):
        temp1 = -1
        temp2 = -1
        for l in range(j,n):
            if j==l:
                temp1 = c[l]
                temp2 = d[l]
            else:
                if temp1<c[l]:
                    temp1 = c[l]
                if temp2 < d[l]:
                    temp2 = d[l]

            diff = abs(temp1 - temp2)
            if diff<=k:
                count += 1

    print("Case #%d: %d"%(i+1,count))