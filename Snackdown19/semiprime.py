def soe(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    nos = list(range(2,n))
    # print(prime)
    # print(nos)
    prime = prime[2:]
    pnos = [nos[i] for i in range(len(nos)) if prime[i]]
    return pnos
def issemi(n):
    s = soe(n)
    x = len(s)
    left = 0
    right = x-1
    f = 0
    while(left<right):
        if (s[left]*s[right])==n:
            return True
        elif (s[left]*s[right]) > n:
            right-=1
        elif (s[left] * s[right]) < n:
            left += 1
    return False

num = list(range(201))
bool = []
for i in num:
    if(issemi(i)):
        bool.append(True)
    else:
        bool.append(False)
sp = [num[i] for i in range(len(num)) if bool[i]]
# print(len(sp))
t = int(input())
for i in range(t):
    n = int(input())
    f = 0
    for j in sp:
        temp = n-j
        if temp in sp:
            f = 1
            break
    if f==1:
        print("YES")
    else:
        print("NO")