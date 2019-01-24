s = input()
ans = []
i=0
while i<len(s):
    if s[i]=='.':
        ans.append('0')
    else:
        if s[i+1]=='.':
            ans.append('1')
        else:
            ans.append('2')
        i=i+1
    i+=1
for j in ans:
    print(j,end='')