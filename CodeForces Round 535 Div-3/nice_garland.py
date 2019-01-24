n = int(input())
si = input()
s = []
for i in si:
    s.append(i)

dic = {0:'R',1:'G',2:'B'}
dic2 = {'R':0,'G':1,'B':2}
c = 0

for i in range(n):
    for j in range(i+1,n):
        if (j-i)%3 == 0:
            continue
        if s[i]==s[j]:
            if (j-3)>=0:
                s[j] = s[j-3]
                c += 1
            elif (j+3)<=n-1:
                s[j] = s[j+3]
                c += 1
            else:
                s[j] = dic[(dic2[s[i]] + 1) % 3]
                c += 1
print(c)
for i in s:
    print(i,end='')