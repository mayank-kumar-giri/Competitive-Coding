n,m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i]<=m:
        arr[i]=0
    else:
        temp = arr[i]
        arr[i] = int(arr[i]/m)
        if temp%m!=0:
            arr[i] += 1

max_index = 0
maxi = -1
for i in range(n):
    if arr[i]>=maxi:
        maxi = arr[i]
        max_index = i
print(max_index+1)