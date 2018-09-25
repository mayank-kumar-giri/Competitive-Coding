fo = open("abalone.data","r+")
c2 = []
for l in fo:
    s = list(l.split(','))
    c2.append(float(s[1]))
n = len(c2)
print(round((sum(c2)/n),6))