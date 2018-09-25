s1 = list(input())
s2 = list(input())
n=len(s1)
for i in range(n):
    if s1[i] not in s2:
        s1.remove(s1[i])
    if s2[i] not in s1:
        s2.remove(s2[i])
print(s1,s2)