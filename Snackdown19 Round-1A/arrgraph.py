from bisect import bisect_left

def bs(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
large_primes = [29, 31, 37, 41, 43, 47]
small_bool = [False]*len(small_primes)

t = int(input())
for l in range(t):
    f = 0
    cp = 0
    g = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in large_primes:
        if bs(a,i) != -1:
            f = 1
            cp = i
            break
    if f==1:# If any large prime is present
        c=0
        for i in a:
            if i%cp==0:
                c+=1
        if c<n: # Large prime is present less than n times
            print("0")
            print(*a)
        elif c==n: # Large prime in whole array(n times)
            g=1
    if g==1:
        # Fill one unique large prime to make it work
        if cp!=47:
            a[0] = 47
        else:
            a[0] = 43
        print("1")
        print(*a)

    if f==0: # No Large Prime(LP) present
        f=0
        for i in small_primes:
            if bs(a, i) != -1:
                cp = i
                small_bool[small_primes.index(cp)] = True
                c=0
                for j in a:
                    if j % cp == 0:
                        c += 1
                if c==1:# Small Prime(SP) present and only 1 multiple of SP (itself) in whole array
                    f=1
            if f==1:
                break
        if f==1:# Small Prime(SP) present and only 1 multiple of SP (itself) in whole array
            print("0")
            print(*a)
        else:# NO Small Prime(SP) present SUCH THAT only 1 multiple of SP (itself) in whole array
            a[0] = 47
            print("1")
            print(*a)