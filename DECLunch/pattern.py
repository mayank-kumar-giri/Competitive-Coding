t = int(input())
for i in range(t):
    n = int(input())
    m = n-1
    arr = []
    # print(arr)
    uparr = list(range(1,n)) + list(range(n-1,0,-1))
    down = 2
    up = 0
    # print(uparr)
    start = 1
    for j in range(n):
        if j>0:
            start += down
            down += 1
        temp = []
        temp2 = start
        for k in range(n):
            if k==0:
                temp.append(temp2)
            else:
                temp2 += uparr[j+k-1]
                temp.append(temp2)
        arr.append(temp)
    # print(arr)
    for j in arr:
        for k in range(len(j)):
            if k!=(len(j)-1):
                print(j[k],end=' ')
            else:
                print(j[k])