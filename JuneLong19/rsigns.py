t = int(input())
mm = 1000000007
for l in range(t):
    k = int(input())
    ans = 1
    base = 2
    while k>0:
        if k%2 == 1:
            ans = ans*base
            k = k-1
        else:
            base = base*base
            k = k//2

    ans = (ans * 5) % mm
    print(ans)