def max_conse(x):
    count = 0
    while x!=0:
        x = (x & (x << 1))
        count += 1
    return count

n,q,k = map(int, input().split())
a = input().replace(' ','')
a = int(a, 2)
query = input()
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
            c = 0
            maxx = 0
            f = 0
            count = 0
            for j in range(reference, n + reference):
                z = j % n
                if a[z] == 1:
                    if f == 0:
                        f = 1
                        c += 1
                    else:
                        c += 1
                else:
                    if f == 1:
                        if maxx <= c:
                            maxx = c
                        c = 0
                        f = 0
                if count == n - 1:
                    if f == 1:
                        if maxx <= c:
                            maxx = c
                        c = 0
                        f = 0
                count += 1
            max_cons = maxx
            if max_cons >= k:
                max_cons = k
            print(max_cons)
            last_ans = max_cons
    qcount += 1
    last_query = i