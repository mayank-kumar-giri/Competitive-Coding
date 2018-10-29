t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = [(b[i]-a[i]) for i in range(n)]
    s = sum(diff)
    if s%6==0:
        exp = s/6
        c = 0
        f = 0
        if (diff[1]<(2*diff[0])) or (diff[2]<(3*diff[0])) or (diff[n-2]%2 != 0) or (diff[n-1]%3 != 0):
            f = 1
        if f:
            print("NIE")
        else:
            print("TAK")
    else:
        print("NIE")