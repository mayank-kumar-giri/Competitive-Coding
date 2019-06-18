t = int(input())
for l in range(t):
    n = int(input())
    arr = input()
    np = 0

    for i in range(n):
        if arr[i]=="P":
            np += 1
    currp = np/n

    if currp>=0.75:
        ans = 0
        print(ans)
        continue

    if n<=4 and currp<0.75:
        print("-1")
        continue

    ans = 0
    flag = 0
    for i in range(2,n-2):
        if arr[i]=="A":
            if ((arr[i-1]=="P" or arr[i-2]=="P") and (arr[i+1]=="P" or arr[i+2]=="P")):
                ans += 1
                np += 1
        currp = np/n
        # print(currp)
        if currp>=0.75:
            flag = 1
            break
    if flag==0:
        print("-1")
    else:
        print(ans)