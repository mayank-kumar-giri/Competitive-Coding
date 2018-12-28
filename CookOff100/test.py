from itertools import *
a = ['G','G','G','R','R','R']
x = []
for i in list(permutations(a,6)):
    if i not in x:
        print(i)
        x.append(i)