t = int(input())
for i in range(t):
    n = int(input())
    p = input()
    ans = ""
    for j in range(0,len(p),2):
        if p[j:j+2]=="SS":
            ans += "EE"
        elif p[j:j+2]=="EE":
            ans += "SS"
        elif p[j:j+2]=="SE":
            ans += "ES"
        else:
            ans += "SE"
    print("Case #%d: %s" % (i + 1,ans))