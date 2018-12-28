n = int(input())
s = input()
revs = s[::-1]

l = 0
r = 0
ls = s[0]
rs = revs[0]
for i in s:
    if i!=ls:
        break
    l += 1
for i in revs:
    if i != rs:
        break
    r += 1

ans = 0
maxi = 998244353
if s[0]!=s[-1]:
    ans = ((l%maxi) + ((r + 1)%maxi))%maxi
else:
    ans = (((l+1)%maxi)*((r+1)%maxi))%maxi

print(ans)