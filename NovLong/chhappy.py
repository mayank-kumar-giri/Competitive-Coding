t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    aso = sorted(a)
    dups = [False]*(n+1)
    elem = [False]*(n+1)
    dups_first_found  = [False]*(n+1)
    for j in range(len(aso)):
        elem[aso[j]] = True
        if j==0:
            continue
        if aso[j]==aso[j-1]:
            dups[aso[j]] = True
    # print(dups)
    # print(elem)
    f = 0
    for j in range(len(a)):
        if dups[a[j]]:
            # print(a[j],dups_first_found[a[j]])
            if dups_first_found[a[j]]==False:
                if elem[j+1]:
                    dups_first_found[a[j]] = True
            else:
                if elem[j+1]:
                    f=1
        if f==1:
            break
    if f==1:
        print("Truly Happy")
    else:
        print("Poor Chef")