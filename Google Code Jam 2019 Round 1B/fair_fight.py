t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    cmaxd = [[-1 for xx in range(n)] for yy in range(n)]
    dmaxd = [[-1 for kk in range(n)] for ll in range(n)]
    count = 0

    for j in range(n):
        for l in range(j,n):
            if j==l:
                cmaxd[j][l] = c[l]
                dmaxd[j][l] = d[l]
            else:
                temp1 = cmaxd[j][l-1]
                temp2 = dmaxd[j][l-1]
                if temp1<c[l]:
                    temp1 = c[l]
                if temp2 < d[l]:
                    temp2 = d[l]
                cmaxd[j][l] = temp1
                dmaxd[j][l] = temp2
            diff = abs(cmaxd[j][l] - dmaxd[j][l])
            if diff<=k:
                count += 1

    print("Case #%d: %d"%(i+1,count))