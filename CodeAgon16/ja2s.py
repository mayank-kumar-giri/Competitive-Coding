def l(s,b,e,memo,str):
    if memo[b][e] != 0:
        print(memo[b][e], str[b][e])
        return (memo[b][e],str[b][e])
    else:
        if b == e:
            memo[b][e] = 1
            str[b][e] = s[b]
            print(memo[b][e],str[b][e])
            return (memo[b][e],str[b][e])
        if e == b + 1:
            if s[b] != s[e]:
                memo[b][e] = 1
                str[b][e] = s[b]
                print(memo[b][e], str[b][e])
                return (memo[b][e],str[b][e])
            else:
                memo[b][e] = 2
                str[b][e] = s[b:e+1]
                print(memo[b][e], str[b][e])
                return (memo[b][e],str[b][e])
        if s[b]==s[e]:
            mtemp,stemp = l(s,b+1,e-1,memo,str)
            memo[b][e] = mtemp + 2
            str[b][e] = s[b]+stemp+s[e]
            print(memo[b][e], str[b][e])
            return (memo[b][e],str[b][e])
        else:
            mtemp1, stemp1 = l(s,b,e-1,memo,str)
            mtemp2, stemp2 = l(s,b+1,e,memo,str)
            memo[b][e] = max(mtemp1,mtemp2)
            if memo[b][e]==mtemp1:
                str[b][e] = stemp1
            else:
                str[b][e] = stemp2
            print(memo[b][e], str[b][e])
            return (memo[b][e],str[b][e])

t = int(input())
for i in range(t):
    a = input()
    b = input()
    x = len(a)
    memo = [[0 for j in range(x)] for k in range(x)]
    str = [["" for j in range(x)] for k in range(x)]
    ac,ass = l(a,0,x-1,memo,str)
    x = len(b)
    memo = [[0 for j in range(x)] for k in range(x)]
    str = [["" for j in range(x)] for k in range(x)]
    bc,bss = l(b,0,x-1,memo,str)

    ans = ac+bc
    if ac%2!=0 and bc%2!=0:
        if ass[int(ac/2)]!=bss[int(bc/2)]:
            ans-=1
    print(ans,ac,bc,ass,bss)