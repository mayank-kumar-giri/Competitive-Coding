def prod(l):
    result = 1
    for i in l:
        result*=i

    return  result
from itertools import combinations
d = {}
l = [i for i in range(1,20)]
result = []
for i in combinations(l,5):
    if sum(i)==22:
        result.append(prod(i))
        d[prod(i)] = list(i)
print(result)
print(max(result))
print(d)
print(d[max(result)])
