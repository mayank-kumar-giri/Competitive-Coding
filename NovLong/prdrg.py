a = list(map(int, input().split()))
t = a[0]
a = a[1:]
for i in a:
    if i==1:
        x = 1
        y = 2
    else:
        e = i-2
        y = 2**i
        if i%2==0:
            x = int((4 ** (int(e / 2) + 1) - 1) / 3)
        else:
            x = int((2*((4 ** (int(e / 2) + 1) - 1) / 3))+1)
    if i==a[len(a)-1]:
        print(x,y,end='')
    else:
        print(x,y,end=' ')