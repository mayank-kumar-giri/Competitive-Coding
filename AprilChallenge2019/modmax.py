n = int(input())
arr = list(sorted(list(map(int, input().split()))))
ans = arr[-1]
f = 0
for i in range(n-1,-1,-1):
    # print(arr[i])
    if arr[i]!=ans:
        ans = arr[i]
        f = 1
        break
if f==0:
    ans = 0
print(ans)