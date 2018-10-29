t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left = n-1
    cap = a[0]
    j = 0
    days = 0
    while left>0:
        left -= cap
        temp = cap
        cap += sum(a[j+1:j+1+cap])
        j += temp
        # print(cap)
        days += 1
    print(days)