import math as m
def circ_right_shift(a):
    temp = list(a)
    for j in range(n - 1):
        temp[j + 1] = a[j]
    temp[0] = a[n - 1]
    a = list(temp)
    return a
n,q,k = map(int, input().split())
a = list(map(int, input().split()))
query = input()

if sum(a)==n:
    for i in query:
        if i=="?":
            print(n)
elif sum(a)==0:
    for i in query:
        if i=="?":
            print("0")
elif "?" not in query:
    pass
else:
    max_a = list(a)
    while max_a[-1]!=0 and max_a[0]!=0:
        # print("CHECK")
        max_a = circ_right_shift(max_a)

    c=0
    sums = []
    f=0
    for j in range(n):

        if max_a[j]==1:
            if f==0:
                f=1
                c+=1
            else:
                c+=1
        else:
            if f==1:
                sums.append(c)
                c=0
                f=0
        if j==n-1:
            if f==1:
                sums.append(c)
                c = 0
                f = 0
    sums.sort()
    maximum = sums[-1]
    if maximum >= k:
        maximum = k
    last = len(sums)-1
    mtom = 0
    for i in range(len(sums)):
        if sums[i]>=k:
            sums[i] = k
            last = i
            break
    if last<len(sums)-1:
        mtom=1
    sums = sums[:last+1]
    sums.reverse()
    maximum = sums[0]
    max2 = 0
    if len(sums)>1:
        if sums[0]==sums[1]:
            mtom = 1
        for i in range(1,len(sums)):
            if sums[i]!=maximum:
                max2 = sums[i]
                break

    ll=0
    ul=0
    done = 0
    f=0
    for j in range(n):
        if a[j]==1:
            if f==0:
                f=1
                ll=j
                c+=1
            else:
                c+=1
        else:
            if f==1:
                if c==maximum:
                    ul=j-1
                    done = 1
                c=0
                f=0
        if j==n-1:
            if f==1:
                if c==maximum:
                    ul=j
                    done = 1
                c = 0
                f = 0
        if done==1:
            break
    if done==0:
        ll=0
        ul=0
        for j in range(n-1,-1,-1):
            if a[j]==0:
                ll=j+1
                break
        for j in range(n):
            if a[j]==0:
                ul=j-1
                break



    # print(maximum,max2,mtom,ll,ul)
    if mtom==1:
        for i in query:
            if i == "?":
                print(maximum)
    else:
        reference = 0
        last_query = ""
        last_ans = 0
        qcount = 0
        for i in query:
            if i=="!":
                if reference==0:
                    reference = n-1
                else:
                    reference -= 1
            else:
                if last_query=="?" and qcount>0:
                    print(last_ans)
                else:
                    maxans = 0
                    if ul<ll:
                        if reference <= ll and reference>ul:
                            maxans = 1
                    else:
                        if reference<=ll or reference>ul:
                            maxans = 1
                    if maximum==1 or maxans==1:
                        print(maximum)
                        last_ans = maximum
                    else:
                        mini = int(m.ceil(maximum/2))
                        if reference<=ul:
                            part = (ul-reference) + 1
                        else:
                            part = (n-reference)+ul+1
                        if part<mini:
                            part = maximum-part
                        max_cons = max(part,max2)
                        print(max_cons)
                        last_ans = max_cons
            qcount += 1
            last_query = i