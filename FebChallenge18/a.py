t = int(input())
for i in range(t):
    s1,s2 = list(input().split(' '))
    if s1[5]>s2[5]:
        print("Second\n")
    elif s1[5]<s2[5]:
        print("First\n")
    else:
        x=s1[0]+s1[1];
        y=s1[3]+s1[4];
        u = s2[0] + s2[1];
        v = s2[3] + s2[4];
        a=int(x)
        b=int(y)
        c=int(u)
        d=int(v)
        if (a==12) and (c!=12):
            print("First\n")
        elif (a!=12) and (c==12):
            print("Second\n")
        else:
            if a>c:
                print("Second\n")
            elif c>a:
                print("First\n")
            else:
                if b > d:
                    print("Second\n")
                elif d > b:
                    print("First\n")



