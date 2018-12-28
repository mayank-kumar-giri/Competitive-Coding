maxi = (10**9)+7
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    kar = [(1+int((n-k)/k))] * k
    left = n%k
    temp = int(n/k)
    ul = temp+int(k/2)
    ll = temp-int(k/2)
    repeat = []
    if ll<1:
        print("-1")
    else:
        if left == 0:
            if k % 2 == 0:
                repeat = list(range(ll, temp)) + list(range(temp + 1, ul + 1))
            else:
                repeat = list(range(ll, ul + 1))
        else:
            if k % 2 == 0:
                h = int(k / 2)
                if left>=h:
                    low = left % h
                else:
                    low = 0
                if left <= h:
                    uhalf = list(range(temp + 1, ul + 1))
                    if left < h:
                        lhalf = list(range(ll, ll + (h - left))) + list(range(ll + (h - left) + 1, ll + h + 1))
                    else:
                        lhalf = list(range(ll + 1, temp + 1))
                else:
                    lhalf = list(range(ll + 1, temp + 1))
                    uhalf = list(range(temp + 1, temp + 1 + (h - low))) + list(range(temp + 2 + (h - low), ul + 2))
                repeat = uhalf + lhalf
            else:
                removed = ll + (k - left)
                repeat = list(range(ll, removed)) + list(range(removed + 1, ul + 2))

        # print(repeat)
        ans = 1
        for j in repeat:
            ans *= j%maxi
            ans *= (j - 1)%maxi
        print(ans % maxi)