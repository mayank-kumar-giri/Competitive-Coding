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
        for j in range(1, m + 1):
            if f == 1:
                break
            for k in range(x):
                if (j % 2) == 0:
                    if 'E' in s:
                        s.remove('E')
                        c += 1
                else:
                    if 'O' in s:
                        s.remove('O')
                        c += 1
                if c >= n:
                    f = 1
                    break
        if c < n:
            print("no")
        else:
            print("yes")


    else:
        print("no")