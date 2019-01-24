n, k = map(int, input().split())
arr = []
sums = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    sums.append(sum(temp))
ans = []
for i in range(k):
    pro = 1
    f=0
    for j in range(len(arr)):
        if f==0 and arr[j][i]==0:
            continue
        else:
            if f==0:
                if j==0:
                    pro *= (arr[j][i]/sums[j])
                else:
                    pro *= (arr[j][i] / (sums[j]+1))
                f=1
            else:
                pro *= ((arr[j][i] + 1)/(sums[j]+1))
    ans.append(pro)
for i in ans:
    print(i,end=' ')