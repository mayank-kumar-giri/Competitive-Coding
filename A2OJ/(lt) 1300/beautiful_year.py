s = input()
sn = int(s)
while True:
    sn += 1
    temp = str(sn)
    f=0
    for i in range(len(temp)-1):
        if temp[i] in temp[i+1:]:
            f=1
            break
    if f==0:
        break
ans = str(sn)
print(ans)