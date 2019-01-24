n,t = map(int, input().split())
string = input()
s = []
for i in string:
    s.append(i)
# print(s,type(s),len(s))
for i in range(t):
    f=0
    for j in range(len(s)-1):
        # print(s[j],s[j+1])
        if f==1:
            f=0
            continue
        if s[j]=='B' and s[j+1]=='G':
            # print(s[j],s[j+1],j,j+1)
            s[j]='G'
            s[j+1]='B'
            # print(s[j],s[j+1],j,j+1)
            f=1
for i in s:
    print(i,end='')