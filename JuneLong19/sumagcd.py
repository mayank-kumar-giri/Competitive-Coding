def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def gcds(arr):
    curr = arr[0]
    for i in range(1,len(arr)):
        curr = gcd(curr,arr[i])
    return curr

from itertools import combinations
t = int(input())
for l in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = 0
    indexes = list(range(n))

    for j in range(1,int(n/2)+1):
        for i in combinations(indexes,j):
            curr = list(i)
            counterpart = [f for f in indexes if f not in curr]
            currf = []
            counterpartf = []
            for k in curr:
                currf.append(arr[k])
            for k in counterpart:
                counterpartf.append(arr[k])
            # print(j, i, currf, counterpartf)
            g1 = gcds(currf)
            g2 = gcds(counterpartf)
            # print(g1,g2)
            ans = g1 + g2

            if maxi<ans:
                maxi = ans

    print(maxi)