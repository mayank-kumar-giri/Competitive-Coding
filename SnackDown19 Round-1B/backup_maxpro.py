maxi = (10**9)+7
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    kar = [(1+int((n-k)/k))] * k
    left = n - (k + (int((n-k)/k) * k))
    kar[0] += left
    extra = 1
    if left==0:
        repeat = kar
        extra=0
    else:
        repeat = kar[1:]
    lr = len(repeat)
    temp = repeat[0]
    ul = temp + int(lr / 2)
    ll = temp - int(lr / 2)
    if ll<1:
        print("-1")
    else:
        repeat = list(range(ll, ul + 1))
        if lr % 2 == 0:
            repeat.remove(temp)
        final_repeat_arr = repeat
        if extra == 1:
            if kar[0] in repeat:
                ul += 1
                ll -= 1
                culprit = repeat.index(kar[0])
                victim = -1 * (culprit+1)
                final_repeat_arr = list(range(ll, ul + 1))
                final_repeat_arr.remove(repeat[victim])
                final_repeat_arr.remove(temp)
                # if lr%2==0:

            else:
                final_repeat_arr = [kar[0]]
                for j in repeat:
                    final_repeat_arr.append(j)
        # print(kar[0],ll,ul,len(repeat),repeat,final_repeat_arr,len(final_repeat_arr),sum(final_repeat_arr))
        ans = 1
        for j in final_repeat_arr:
            ans *= j%maxi
            ans *= (j - 1)%maxi
        print(ans % maxi)