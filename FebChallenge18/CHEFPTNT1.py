t = int(input())
for i in range(t):
    n, m, x, k = map(int, input().split(' '))
    s = list(input())
    if k >= n:
        if m < n and x < 2:
            print("no")
            continue
        c = 0
        f = 0
        ce = 0
        co = 0

        for l in s:
            if l == 'E':
                ce += 1
            else:
                co += 1
        for j in range(1, m + 1):
            if f == 1:
                break
            for k in range(x):
                if (j % 2) == 0:
                    if ce>0:
                        ce=ce-1
                        c=c+1
                else:
                    if co>0:
                        co=co-1
                        c=c+1
                if c >= n:
                    f = 1
                    break
                if ce==0 and co==0:
                    f=1
                    break
        if c < n:
            print("no")
        else:
            print("yes")
    else:
        print("no") 