t = int(input())
for l in range(t):
    n = int(input())
    c = 0
    temp = n
    ds = 0
    while temp != 0:
        # print(temp, ds)
        ds += (temp % 10)
        temp = temp//10


    # print(ds)

    if ds%10==0:
        digit = 0
    else:
        digit = 10 - ds%10

    # print(digit)
    ans = int(str(n) + str(digit))
    print(ans)