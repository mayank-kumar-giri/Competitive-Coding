def ft(n):
    if n==0:
        return 1
    if n<0:
        return -1
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def ncr(n,r):
    ans = (ft(n)/(ft(n-r)*ft(r)))
    if ans<=0:
        return -1
    return ans

x = int(input())
s = int(input())
y = int(input())
m = int(input())
z = int(input())
c = int(input())
a,b = input().split()
a = ord(a) - ord('A')
b = ord(b) - ord('A')

normal = ncr(x,s) * ncr(y,m) * ncr(z,c)

q1 = x-1
q2 = x+y - 1

if (a<=q1 and b<=q2):
    x -= 1
    ans = ncr(x, s) * ncr(y, m) * ncr(z, c)
elif (a<=q2 and b<=q2):
    y -= 1
    ans = ncr(x, s) * ncr(y, m) * ncr(z, c)
elif (a>q2 and b>q2):
    z -= 1
    ans = ncr(x, s) * ncr(y, m) * ncr(z, c)
else:
    if a<=q1:
        aa = 0
    elif a<=q2:
        aa = 1
    else:
        aa = 2

    if b <= q1:
        bb = 0
    elif b <= q2:
        bb = 1
    else:
        bb = 2

    if aa==0 and bb==1:
        ans = (ncr(x-1, s) * ncr(y, m) * ncr(z, c)) + (1 * ncr(y, m) * ncr(z, c))