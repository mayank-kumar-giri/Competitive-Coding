n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
left = n%s
if left==0:
    left = s
    for i in range(7):
        left -= arr[i]
        if left<1:
            print(i+1)
            break
else:
    for i in range(7):
        left -= arr[i]
        if left<1:
            print(i+1)
            break