n,k = map(int, input().split())
s = list(map(int, input().split()))
ans = n
for i in range(n):
    for j in range(i+1,n):
        diff = abs(s[i]-s[j])
        if diff<=k:
            ans+=1
print(ans)