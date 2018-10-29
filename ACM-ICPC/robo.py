t= int(input())
for i in range(t):
    s = input()
    n = len(s)
    prev = ""
    curr = ""
    previndex = -1
    currindex = -1
    for j in s:
        prev = curr
        previndex = currindex
        if j!=".":
            curr = int(j)
            currindex = s.index(j)
        if prev!="":
            if prev