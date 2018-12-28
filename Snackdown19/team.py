maxi = 1000000007
def p(n):
    if n<=2:
        return 1
    else:
        temp = n-1
        vari = n-1
        while vari!=1:
            vari-=2
            temp = (temp * vari)
        return temp

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    # print(s)
    f = 0
    c = 0
    ans = 1
    for j in range(1,n):
        # print(n,j,c,f)
        if f==0 and s[j]==s[j-1]:
            f = 1
            c = 2
        elif f==1 and  s[j]==s[j-1]:
            c += 1
        elif f==1 and s[j]!=s[j-1]:
            f = 0
            temp = 0
            if c%2 == 0:
                temp = p(c)
            else:
                temp = (c%maxi) * (p(c-1)%maxi)
                temp = temp%maxi
            # print("temp",temp)
            ans = (ans*temp)%maxi
            c = 0
    print(ans)