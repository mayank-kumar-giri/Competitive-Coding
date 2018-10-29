t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    # print(s)
    c = k
    for j in range(k,n):
        if s[j]==s[k-1]:
            c+=1
        else:
            break
    print(c)
