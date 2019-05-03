t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    neg = 0
    zero = 0
    pos = 0
    for j in arr:
        if j<0:
            neg+=1
        elif j==0:
            zero+=1
        else:
            pos+=1
    maxi = max(pos,neg)+zero
    if min(pos,neg)==0:
        mini = maxi
    else:
        mini = min(pos,neg)
    print(maxi,mini)
