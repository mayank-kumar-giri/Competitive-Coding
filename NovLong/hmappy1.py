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

max_a = list(a)
while max_a[-1]!=0 and max_a[0]!=0:
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

print(len(sums),sums,sums[0],sums[-1])

last = len(sums)-1
g=0
nom = 0
try:
    maximum = max(sums)
except:
    maximum = 0
if maximum==0:
    for i in query:
        if i=="?":
            print(maximum)
else:
    if maximum >= k:
        maximum = k
    for i in range(len(sums)):
        if sums[i] >= maximum:
            sums[i] = maximum
            nom = nom + 1
            if g == 0:
                g = 1
                last = i


    if sums[-1] > 1:
        mini = int(m.ceil(sums[-1] / 2))
    else:
        mini = sums[-1]

    first = 0
    for i in range(len(sums)):
        # print("SHIT",i,sums[i])
        if sums[i] >= mini:
            first = i
            break

    sums = sums[first:last + 1]
    print("sums",sums)
#-----------------------------------------------------------------------
    c = 0
    maxx = -1
    index = 0
    f = 0
    for j in range(n):
        if a[j] == 1:
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
        if j == n - 1:
            if f == 1:
                if maxx <= c:
                    maxx = c
                c = 0
                f = 0
        if maxx == maximum:
            index = j
            break

    left = n - index
    count = 0
    # print("left",left,"index",index)
    # print(max_a,"\n",sums,maximum,left,nom)
    if nom > 1:
        for i in query:
            if i == "?":
                print(maximum, end=' ')
    else:
        for i in query:
            if i == "!":
                count += 1
            else:
                actual = count % n
                if actual <= left:
                    print(maximum, end=' ')
                else:
                    actual = actual - left
                    tem = list(sums)
                    # print("final check", maximum)
                    if actual < maximum:
                        if actual >= mini:
                            tem[-1] = actual
                        else:
                            tem[-1] = maximum - actual
                    # print("tem", tem)
                    ans = max(tem)
                    print(ans, end=' ')