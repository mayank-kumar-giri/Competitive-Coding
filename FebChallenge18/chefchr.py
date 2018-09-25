t=int(input())
for i in range(t):
    s=list(input())
    c=0
    tc=0
    n=len(s)



    b=['c','e','f','h']
    if n>=4:
        for j in range(n-3):
            b = ['c', 'e', 'f', 'h']
            f=0


            for k in range(4):
                if s[j+k] not in b:
                    f=1
                    break
                else:
                    b.remove(s[j+k])

            if f!=1:
                c+=1
        if c>0:
            print("lovely",c)
        else:
            print("normal")
    else:
        print("normal")
