from operator import itemgetter
t = int(input())
for l in range(t):
    d = int(input())
    s = []
    for i in range(d):
        temp = list(map(int, input().split()))
        s.append(temp)
    s_sorted = list(sorted(s,key=itemgetter(0)))
    # print(s_sorted)
    q = int(input())
    queries = []
    for j in range(q):
        temp = list(map(int, input().split()))
        queries.append(temp)
    for k in queries:
        sum = 0
        for m in s_sorted:
            if m[0]>k[0]:
                break
            else:
                sum+=m[1]
            if sum>=k[1]:
                break
        # print(sum)
        if sum>=k[1]:
            print("Go Camp")
        else:
            print("Go Sleep")