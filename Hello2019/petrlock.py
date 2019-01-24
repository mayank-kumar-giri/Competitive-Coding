n = int(input())
arr = []
for z in range(n):
    arr.append(int(input()))

arr = list(sorted(arr))

i=1
j=n-2

c1 = arr[0]
c2 = arr[-1]

while i<j:
    if c1<c2:
        c1+=arr[i]
        i+=1
    else:
        c2+=arr[j]
        j-=1
diff = abs(c1-c2)
if i==j:
    diff+=arr[i]

if (360-(diff%360))%2==0:
    print("YES")
else:
    print("NO")