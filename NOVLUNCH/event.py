days = dict({"sunday":1,"monday":2,"tuesday":3,"wednesday":4,"thursday":5,"friday":6,"saturday":7})
t = int(input())
for i in range(t):
    s,e,l,r = input().split()
    l = int(l)
    r = int(r)

    dur = 0
    s_num = days[s]
    e_num = days[e]

    if e_num>s_num:
        dur = (e_num - s_num) + 1
        dur = dur%7
    elif e_num==s_num:
        dur = 1
    else:
        dur = (7 - abs(e_num-s_num)) + 1
        dur = dur%7



    count = 0
    for j in range(l,r+1):
        temp = j%7
        if dur==temp:
            count += 1

    # print(s_num, e_num, dur, count)

    if count==0:
        print("impossible")
    elif count==1:
        ans = 0
        for j in range(l, r + 1):
            if j%7==dur:
                ans = j
        print(ans)
    else:
        print("many")