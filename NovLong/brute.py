n,q,k = map(int, input().split())
a = list(map(int, input().split()))
query = input()
# print(a)
for i in query:
    if i=="!":
        temp = list(a)
        for j in range(n-1):
            temp[j+1] = a[j]
        temp[0] = a[n-1]
        a = list(temp)
        # print("a",a)
    else:
        c=0
        maxx = 0
        f=0
        for j in range(n):
            if a[j]==1:
                if f==0:
                    f=1
                    c+=1
                else:
                    c+=1
            else:
                if f==1:
                    if maxx<=c:
                        maxx = c
                    c=0
                    f=0
            if j==n-1:
                if f==1:
                    if maxx<=c:
                        maxx = c
                    c = 0
                    f = 0
        # print("sums",sums)
        max_cons = maxx
        if max_cons>=k:
            max_cons=k
        print(max_cons,end=' ')