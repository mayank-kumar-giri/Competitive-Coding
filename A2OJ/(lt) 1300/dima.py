n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
c = 0
for i in range(1,6):
    t = s
    t += i
    if t%(n+1)==1:
        continue
    else:
        c+=1
print(c)