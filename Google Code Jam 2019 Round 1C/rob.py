t = int(input())
for i in range(t):
    a = int(input())
    prog = []
    maxi = 0
    for j in range(a):
        prog.append(input())
        if len(prog[-1])>maxi:
            maxi = len(prog[-1])
    dic = {'R':0,'P':0,'S':0}
    win = {'R': 'P', 'P': 'S', 'S': 'R'}
    ans = ""
    for k in range(maxi):
        dic = {'R': 0, 'P': 0, 'S': 0}
        for l in range(0,a):
            if (prog[l][k%len(prog[l])] == 'R') and (dic['R']==0):
                dic['R'] = 1
            elif (prog[l][k % len(prog[l])] == 'P') and (dic['P']==0):
                dic['P'] = 1
            elif (prog[l][k % len(prog[l])] == 'S') and (dic['S']==0):
                dic['S'] = 1
        # print(dic)
        if dic['R']==1 and dic['P']==1 and dic['S']==1:
            ans = "IMPOSSIBLE"
            break
        elif dic['R']==1 and dic['P']==1:
            ans += "P"
        elif dic['R'] == 1 and dic['S'] == 1:
            ans += "R"
        elif dic['S'] == 1 and dic['P'] == 1:
            ans += "S"
        else:
            ans += win[prog[0][k%len(prog[0])]]
            break

    print("Case #%d: %s" % (i+1,ans))