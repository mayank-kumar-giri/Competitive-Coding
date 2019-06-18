t = int(input())
for l in range(t):
    n = int(input())
    c = 0
    if n<=9:
        curr=19
        nc = n
    else:
        ttt = n-9
        h = ttt//10
        curr = (h+1)*100
        nc = ttt%10
    while c!=nc:
        temp = curr
        ds = 0

        while temp!=0:
            ds += (temp%10)
            temp = int(temp/10)

        if (ds%10) == 0:
            c += 1
            # print(curr)
        if c==nc:
            break

        curr += 1
        # print(c,curr,ds,temp)

    ans = curr
    print(ans)