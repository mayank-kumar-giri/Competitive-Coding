t = int(input())
for i in range(t):
    n,d = input().split()
    d = int(d)
    digits = []
    for j in n:
        digits.append(int(j))
    # print(digits)
    currl = 0
    currr = len(digits)
    fnum = {}
    count = 0
    # print(digits)
    while currl<currr:
        # print(currl, currr, mind, count)
        mind = min(digits[currl:currr])
        if mind>=d:
            count += (currr - currl)
            break
        lasti = currl
        nt = 0
        for j in range(len(digits[currl:currr])):
            if digits[currl:currr][j]==mind:
                nt+=1
                lasti = j
        fnum[mind] = nt
        count += (lasti + 1 - nt)
        currl = currl + lasti + 1
        # print(currl,currr,mind,count)

    # print(fnum)
    numlist = sorted(list(fnum.keys()))
    if not numlist:
        ans = [d]*len(digits)
    else:
        ans = []
        for j in numlist:
            ans = ans + [j]*fnum[j]
        ans = ans + [d]*count

    for j in ans:
        print(j,end='')
    print('')