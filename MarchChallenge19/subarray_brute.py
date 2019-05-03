from collections import Counter

t = int(input())
for i in range(t):
    solution = []
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for j in range(1,n+1):
        for l in range(0,n-j+1):
            curr = arr[l:(l+j)]
            curr = sorted(curr)
            # print(curr)
            # currdic = Counter(curr)
            # vals = list(currdic.values())
            m = int(k/j) + 1
            # sum = 0
            # for x in currdic:
            #     sum += (m*currdic[x])
            #     if sum>=k:
            #         X = x
            #         break
            if k%m==0:
                index = int(k/m)-1
            else:
                index = int(k/m)
            X = curr[index]
            F = curr.count(X)
            if F in curr:
                ans += 1
                solution.append([curr,"YES"])
            else:
                solution.append([curr,"NO"])
    print(ans)
    for x in solution:
        print(x)