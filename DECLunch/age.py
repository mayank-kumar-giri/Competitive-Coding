t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dc = sum(arr)
    ldc = dc + 1
    bday = list(map(int, input().split()))
    curr = list(map(int, input().split()))
    ll = bday[0]+1
    ul = curr[0]-1
    if bday[0]==curr[0]:
        if (curr[1]-bday[1])>0:
            age = (arr[bday[1] - 1] - bday[2]) + 1 + curr[2]
            if (curr[1]-bday[1])>1:
                age += sum(arr[bday[1]:(curr[1]-1)])
        else:
            age = curr[2]-bday[2] + 1
        # print("here",sum(arr[bday[1]:curr[1]]),((arr[bday[1]-1]-bday[2])+1),curr[2],age)
    elif ll<=ul:
        if ll==ul:
            by = sum(arr[bday[1]:]) + (arr[bday[1] - 1] - bday[2]) + 1
            cy = sum(arr[:(curr[1] - 1)]) + curr[2]
            if ll%4==0:
                x = ll * ldc
            else:
                x = ll * dc
            age = by + cy + x
        else:
            by = sum(arr[bday[1]:]) + (arr[bday[1] - 1] - bday[2]) + 1
            cy = sum(arr[:(curr[1] - 1)]) + curr[2]
            totalyrs = ul-ll+1
            if ll%4==0:
                lll = ll
            else:
                lll = ll + (4-ll%4)
            if ul%4==0:
                lul = ul
            else:
                lul = ul - (ul%4)
            totalleaps = int((lul-lll)/4) + 1
            totalnormals = totalyrs - totalleaps
            age = by + cy + (totalnormals*dc) + (totalleaps * ldc)
            print(by, cy,totalleaps,totalnormals,totalyrs,dc,ldc, (totalnormals * dc), (totalleaps * ldc))
    else:
        by = sum(arr[bday[1]:]) + (arr[bday[1] - 1] - bday[2]) + 1
        cy = sum(arr[:(curr[1] - 1)]) + curr[2]
        # print(by,cy)
        age = by + cy

    print(age)