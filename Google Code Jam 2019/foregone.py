t = int(input())
for i in range(t):
    n = int(input())
    digits = []
    d = 0
    temp = n
    while temp != 0:
        digits.append(temp%10)
        temp = int(temp/10)
        d+=1
    a = 0
    for j in range(d):
        if digits[j]==4:
            a += (10**j)
    b = n-a
    # print(digits)
    print("Case #%d: %d %d" % (i+1,a,b))