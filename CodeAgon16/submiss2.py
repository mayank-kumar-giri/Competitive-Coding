def l(s,b,e,memo,str):
    if memo[b][e] != 0:
        return (memo[b][e],str[b][e])
    else:
        if b == e:
            memo[b][e] = 1
            str[b][e] = [s[b]]
            print(memo[b][e],str[b][e])
            return (memo[b][e],str[b][e])
        if e == b + 1:
            if s[b] != s[e]:
                memo[b][e] = 1
                str[b][e] = [s[b]]
                str[b][e].append(s[e])
                print(memo[b][e],str[b][e])
                return (memo[b][e],str[b][e])
            else:
                memo[b][e] = 2
                str[b][e] = [s[b:e+1]]
                print(memo[b][e],str[b][e])
                return (memo[b][e],str[b][e])
        if s[b]==s[e]:
            mtemp,stemp = l(s,b+1,e-1,memo,str)
            memo[b][e] = mtemp + 2
            for i in range(len(stemp)):
                stemp[i] = s[b]+stemp[i]+s[e]
            str[b][e] = stemp
            print(memo[b][e],str[b][e])
            return (memo[b][e],str[b][e])
        else:
            mtemp1, stemp1 = l(s,b,e-1,memo,str)
            mtemp2, stemp2 = l(s,b+1,e,memo,str)
            memo[b][e] = max(mtemp1,mtemp2)
            if mtemp1==mtemp2:
                str[b][e] = stemp1
                for each in range(len(stemp2)):
                    if stemp2[each] not in str[b][e]:
                        str[b][e].append(stemp2[each])
            elif memo[b][e]==mtemp1:
                str[b][e] = stemp1
            else:
                str[b][e] = stemp2
            print(memo[b][e],str[b][e])
            return (memo[b][e],str[b][e])

t = int(input())
for i in range(t):
    a = input()
    b = input()

    x = len(a)
    memo = [[0 for j in range(x)] for k in range(x)]
    str = [[[""] for j in range(x)] for k in range(x)]
    ac,ass = l(a,0,x-1,memo,str)

    x = len(b)
    memo = [[0 for j in range(x)] for k in range(x)]
    str = [[[""] for j in range(x)] for k in range(x)]
    bc, bss = l(b, 0, x - 1, memo, str)

    ans = ac+bc
    f=0
    if ac%2!=0 and bc%2!=0:
        for i in ass:
            for j in bss:
                if i[int(ac / 2)] == j[int(bc / 2)]:
                    f=1
                if f==1:
                    break
            if f==1:
                break
        if f==0:
            ans-=1
    print(ans)