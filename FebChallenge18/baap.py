import random as r
def rr(ind,l):
    a = r.choice(l)
    while a == ' ?':
        a=r.choice(l)
    l[ind] = a
fo = open("t.data","r+")
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
c10 = []
c11 = []
c12 = []
c13 = []
c14 = []
c15 = []
nl = 0
for l in fo:
    a = list(l.split(','))
    c1.append(a[0])
    c2.append(a[1])
    c3.append(a[2])
    c4.append(a[3])
    c5.append(a[4])
    c6.append(a[5])
    c7.append(a[6])
    c8.append(a[7])
    c9.append(a[8])
    c10.append(a[9])
    c11.append(a[10])
    c12.append(a[11])
    c13.append(a[12])
    c14.append(a[13])
    c15.append(a[14])

    nl = nl + 1
print(c2)
for i in range(nl):
    if c1[i] == ' ?':
        rr(i,c1)
    if c2[i] == ' ?':
        rr(i,c2)
    if c3[i] == ' ?':
        rr(i,c3)
    if c4[i] == ' ?':
        rr(i,c4)
    if c5[i] == ' ?':
        rr(i,c5)
    if c6[i] == ' ?':
        rr(i,c6)
    if c7[i] == ' ?':
        rr(i,c7)
    if c8[i] == ' ?':
        rr(i,c8)
    if c9[i] == ' ?':
        rr(i,c9)
    if c10[i] == ' ?':
        rr(i,c10)
    if c11[i] == ' ?':
        rr(i,c11)
    if c12[i] == ' ?':
        rr(i,c12)
    if c13[i] == ' ?':
        rr(i,c13)
    if c14[i] == ' ?':
        rr(i,c14)
    if c15[i] == ' ?':
        rr(i,c15)

sltmp = [c1[0],',',c2[0],',',c3[0],',',c4[0],',',c5[0],',',c6[0],',',c7[0],',',c8[0],',',c9[0],',',c10[0],',',c11[0],',',c12[0],',',c13[0],',',c14[0],',',c15[0]]
fo.close()
f = open('t.data', 'w')
f.close()
ab = open("t.data","r+")
ab.writelines(sltmp)
ab.close()
cd = open("t.data","a+")
for j in range(1,nl):
    sl = [c1[j],',',c2[j],',',c3[j],',',c4[j],',',c5[j],',',c6[j],',',c7[j],',',c8[j],',',c9[j],',',c10[j],',',c11[j],',',c12[j],',',c13[j],',',c14[j],',',c15[j]]
    cd.seek(0,2)
    cd.writelines(sl)
cd.close()