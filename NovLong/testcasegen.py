import random as r
n = r.randint(1,5000)
q = r.randint(1,5000)
k = r.randint(1,n)
a = []
for i in range(n):
    a.append(r.randint(0,1))
qu = []
for j in range(q):
    qu.append(r.choice(["!","?"]))
print(n,q,k)
for i in range(n):
    if i!=n-1:
        print(a[i],end=' ')
    else:
        print(a[i])
for i in range(q):
    if i!=q-1:
        print(qu[i],end='')
    else:
        print(qu[i])