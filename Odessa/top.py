s = list(S)

ans = []

for i in range(n):
    count = 0
    for j in range(i+1,n):
        if s[j]<s[i]:
            count+=1
    ans.append(count)

return ans