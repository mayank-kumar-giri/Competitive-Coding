t = int(input())
for i in range(t):
    n,a,b = map(int, input().split())
    arr = list(map(int, input().split()))
    bob = 0
    alice = 0
    common = 0
    for j in arr:
        if j%a==0:
            bob+=1
        if j%b==0:
            alice+=1
        if j%a==0 and j%b==0:
            common+=1

    if alice>bob:
        print("ALICE")
    elif bob>alice:
        print("BOB")
    else:
        if common!=0:
            print("BOB")
        else:
            print("ALICE")