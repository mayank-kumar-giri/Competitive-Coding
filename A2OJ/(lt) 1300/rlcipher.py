s = input()
n = len(s)
cs = ["z"]*n
if n%2==0:
    m = int(n/2) - 1
else:
    m = int(n/2)
pp = m + 1
np = m - 1

cs[0] = s[m]
i=1
while i<n:
    cs[i] = s[pp]
    i+=1
    if i>=n:
        break
    cs[i] = s[np]
    i+=1
    pp+=1
    np-=1
ans = ""
for i in cs:
    ans = ans+i
print(ans)