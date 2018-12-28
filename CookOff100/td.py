t = int(input())
for i in range(t):
    tr = int(input())
    ttr = list(map(int, input().split()))
    dr = int(input())
    ddr = list(map(int, input().split()))
    ts = int(input())
    tts = list(map(int, input().split()))
    ds = int(input())
    dds = list(map(int, input().split()))
    r = ttr + ddr
    s = tts + dds
    arr = [False] * 101
    for j in ttr:
        arr[j] = True
    f = 0
    for j in tts:
        if arr[j]==False:
            f=1
            break
    if f:
        print("no")
    else:
        brr = [False] * 101
        for j in ddr:
            brr[j] = True
        f = 0
        for j in dds:
            if brr[j] == False:
                f = 1
                break
        if f:
            print("no")
        else:
            print("yes")