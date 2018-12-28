import time

t = int(input())
for l in range(t):
    start = time.perf_counter()
    ns = input()
    le = len(ns)
    n = int(ns)
    j = 1
    yno = str(ns)
    while j<le:
        yno += ns[j:]
        yno += ns[:j]
        j+=1
    ans = int(yno) % ((10**9)+7)
    print(ans)
    print(time.perf_counter()-start)