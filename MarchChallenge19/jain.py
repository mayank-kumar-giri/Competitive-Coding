from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    dishes = []
    for j in range(n):
        dishes.append(input().strip())
    ds = []
    vowels = {"a":16,"e":8,"i":4,"o":2,"u":1}
    for j in dishes:
        num = 0
        for k in j:
            num = num | vowels[k]
        ds.append(num)

    ddict = Counter(ds)
    keylist = sorted(list(ddict.keys()))
    liked = 0

    # print(ds,ddict,keylist,len(keylist))
    for j in range(len(keylist)):
        for k in range(j+1,len(keylist)):
            # if (keylist[j] | keylist[k])==31:
            #     print(keylist[j],keylist[k],(keylist[j] | keylist[k])==31)
            if (keylist[j] | keylist[k])==31:
                liked += (ddict[keylist[j]]*ddict[keylist[k]])
    for j in range(len(keylist)):
        if ddict[keylist[j]]<2:
            continue
        if (keylist[j] | keylist[j]) == 31:
            liked += int((ddict[keylist[j]] * (ddict[keylist[j]]-1))/2)

    print(liked)