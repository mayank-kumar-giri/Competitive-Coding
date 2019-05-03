t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mini = 999999999
    for j in a:
        temp = list(a)
        for k in range(n):
            temp[k] = temp[k] ^ j
        s = sum(temp)
        if mini>s:
            mini = s
    print(mini)