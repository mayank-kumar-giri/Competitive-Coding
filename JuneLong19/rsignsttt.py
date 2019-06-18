c=0
for i in range(10**1000000000):

    a = set()
    temp = i
    while temp != 0:
        a.add(temp % 10)
        temp = temp//10
    temp = (10**1000000000)-i-1
    while temp != 0:
        a.add(temp % 10)
        temp = temp//10
    if len(a)==2 or len(a)==1:
        c+=1
print(c)