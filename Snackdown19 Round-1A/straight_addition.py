import math as m
import itertools as it

def perm(s):
    l = []
    for i in s:
        l.append(i)
    return set(list(it.permutations(l,len(l))))
t = int(input())
for i in range(t):
    a,b,c = map(int , input().split())
    # print("LOG",m.floor(m.log2(c-1)))
    k = int(m.floor(m.log2(c-1))) + 1
    if k<=1:
        k=2
    bina = bin(a)[2:].zfill(k)
    temp_perms = perm(bina)
    perms = []
    for j in temp_perms:
        temp=""
        for l in j:
            temp += l
        dec_temp = int(temp,2)
        if dec_temp<=(c-1) and dec_temp>=1:
            perms.append(temp)
    # print(perms)
    binb = bin(b)[2:].zfill(k)
    n0b = 0
    n1b = 0
    for j in binb:
        if j=="0":
            n0b+=1
        else:
            n1b+=1
    # print(bina,binb)
    # print("n0",n0b,"n1",n1b,k)
    boolean = []
    for j in perms:
        temp_0 = 0
        temp_1 = 0
        temp_j = ""
        for l in j:
            temp_j += l
        dec_j = int(temp_j,2)
        cminusj = c-dec_j
        bincmj = bin(cminusj)[2:].zfill(k)
        # print("HIGH CHECK",temp_j,dec_j,cminusj,bincmj)
        # print("CHECK",binb,bincmj)
        for l in bincmj:
            if l=="0":
                temp_0 += 1
            else:
                temp_1 += 1
        if n1b==temp_1 and n0b==temp_0:
            boolean.append(True)
        else:
            boolean.append(False)
    ans = 0
    for j in boolean:
        if j==True:
            ans+=1
    print(ans)