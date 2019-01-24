from collections import Counter
n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr,reverse=True)

a = arr[0]
b = -1
for i in range(n):
    if (a%arr[i])!=0:
        b = arr[i]
        break

dic = Counter(arr)
print(dic)
if b==-1:
    for i in range(n):
        if dic[arr[i]]==2:
            b = arr[i]

print(a,b)