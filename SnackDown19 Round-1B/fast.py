maxi = (10**9)+7
t=int(input())
for i in range(t):
    ans=1;
    n,k=map(int,input().split())
    temp=k*(k+1)/2
    if(temp>n):
        print("-1")
    else:
        a=list(range(1,k+1))
        left = n-temp
        inc = int(left/k)
        l_inc = int(left%k)
        for j in range(len(a)):
            a[j] += inc
        for j in range(int(l_inc)):
            a[-1*(j+1)]+=1
        ans = 1
        for j in a:
            ans *= (j%maxi * (j-1)%maxi)%maxi
        ans = ans%maxi
        print(ans)