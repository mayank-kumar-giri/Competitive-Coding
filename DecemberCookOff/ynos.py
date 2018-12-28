import time
t = int(input())
for l in range(t):
    start = time.perf_counter()
    ns = input()
    le = len(ns)
    n = int(ns)
    dic = {}
    for i in range(le):
        dic[i] = ns[i]
    fs = ["z"]*(le**2)
    for i in range(le):
        fs[i] = ns[i]
    cp = le
    for i in range(1,le):
        cs = i
        for j in range(le):
            fs[cp] = dic[cs]
            cp += 1
            cs = (cs+1)%le
    # po = (le**2)-1
    # ans = 0
    maxi = (10**9)+7
    # for i in fs:
    #     ans += (int(i)*(10**po))%maxi
    #     po-=1
    # ans = ans%maxi
    final = ""
    for i in fs:
        final += i
    ans = int(final) % maxi

    print(ans)
    print(time.perf_counter()-start)