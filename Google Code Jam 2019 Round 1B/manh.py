t = int(input())
for i in range(t):
    p,q = map(int, input().split())
    manhattan = [[0 for xx in range(q+1)] for yy in range(q+1)]
    for j in range(p):
        x,y,d = input().split()
        x = int(x)
        y = int(y)

        if d=='S':
            for k in range(q+1):
                for l in range(y):
                    manhattan[k][l] += 1
        elif d=='W':
            for k in range(x):
                for l in range(q+1):
                    manhattan[k][l] += 1
        elif d=='N':
            for k in range(q+1):
                for l in range(y+1,q+1):
                    manhattan[k][l] += 1
        elif d == 'E':
            for k in range(x+1,q+1):
                for l in range(q+1):
                    manhattan[k][l] += 1

    maxi = -1
    ansx = -1
    ansy = -1
    for j in range(q+1):
        for k in range(q+1):
            if maxi<manhattan[j][k]:
                maxi = manhattan[j][k]
                ansx = j
                ansy = k

    print("Case #%d: %d %d"%(i+1,ansx,ansy))