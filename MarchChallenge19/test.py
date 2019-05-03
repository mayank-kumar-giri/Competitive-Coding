import random as r
s = ["a","e","i","o","u"]
li = []
for i in range(r.randint(1,20)):
    temp = ""
    for j in range(r.randint(1,10)):
        temp += r.choice(s)
    li.append(temp)
print(len(li))
for i in li:
    print(i)
# print(30 | 28)