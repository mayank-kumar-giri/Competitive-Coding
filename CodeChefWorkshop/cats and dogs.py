t = int(input())
for i in range(t):
    c,d,l = map(int, input().split())
    if (l%4)!=0:
        print("no")
        continue
    else:
        left = l - (4*d)
        cg = int(left/4)
        if cg>c or cg<0:
            print("no")
            continue
        cr = c-cg
        if cr>(2*d):
            print("no")
            continue
        print("yes")