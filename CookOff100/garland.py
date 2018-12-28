t = int(input())
for i in range(t):
    s = input()
    if (len(s)%2)==1:
        print("no")
    else:
        rc = 0
        gc = 0
        r = 0
        g = 0
        rr = 0
        gg = 0
        for j in s:
            if j=='R':
                if g==1:
                    g=0
                if r==0:
                    r=1
                else:
                    rr+=1
                rc+=1
            else:
                if r==1:
                    r=0
                if g==0:
                    g=1
                else:
                    gg+=1
                gc+=1
        if s[0]==s[len(s)-1]:
            if s[0]=='R':
                rr+=1
            else:
                gg+=1
        if rc!=gc:
            print("no")
        else:
            if rr>1 or gg>1:
                print("no")
            else:
                print("yes")