n = int(input())
xy = {}
yx = {}
points = []
for i in range(n):
    tx,ty = map(int, input().split())
    points.append([tx,ty])
    if tx in xy:
        if ty not in xy[tx]:
            xy[tx].append(ty)
    else:
        xy[tx] = [ty]
    if ty in yx:
        if tx not in yx[ty]:
            yx[ty].append(tx)
    else:
        yx[ty] = [tx]

supcents = 0
for i in points:
    temp = list(sorted(xy[i[0]]))
    cyi = temp.index(i[1])
    if cyi>0 and cyi<(len(temp)-1):
        pass
    else:
        continue
    temp = list(sorted(yx[i[1]]))
    cxi = temp.index(i[0])
    if cxi > 0 and cxi < (len(temp) - 1):
        supcents+=1
print(supcents)