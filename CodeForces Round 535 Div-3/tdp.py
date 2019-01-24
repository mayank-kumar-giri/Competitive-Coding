q = int(input())
for i in range(q):
    l1,r1,l2,r2 = map(int, input().split())
    if l2 < l1 and r2 < r1:
        print(l1, l2)
    else:
        print(l1,r2)
