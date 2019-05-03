tags = set()
fo = open("b_lovely_landscapes.txt","r")
photos = []
for i in fo:
    photos.append(i)

for i in range(len(photos)):
    x = len(photos[i])
    photos[i] = photos[i][:x-1]
n = int(photos[0])
# n = n-1
photos = photos[1:]

for i in range(len(photos)):
    photos[i] = list(photos[i].split(" "))
    for j in range(2,len(photos[i])):
        tags.add(photos[i][j])
tags = list(tags)
t = len(tags)
tagvalue = {}
valuetag = {}
for i in range(t):
    tagvalue[tags[i]] = i
    valuetag[i] = tags[i]
# print(tags)

matrix = [set() for y in range(n)]
# print(photos)

for i in range(n):
    temp = photos[i][2:]
    for k in temp:
        matrix[i].add(k)
# print(matrix)

# print(matrix)
#
from itertools import combinations

Slides = []
Slides.append(0)
used = [False]*n
used[0] = True

for i in range(n):
    print("Iteration -",i)
    if i!=0:
        if used[i]:
            continue
        else:
            Slides.append(i)
            used[i]=True

    present = []
    temp = list(matrix[i])
    for j in range(len(temp)):
        present.append(tagvalue[temp[j]])
    # print(present)

    prcombs = list(combinations(present,int(len(present)/2)))
    # print(prcombs,"\n")

    for j in prcombs:
        cl = len(j)
        grandflag = 0
        for k in range(i+1,n):
            if used[k]:
                continue
            flag = 0
            for l in range(cl):
                temp = valuetag[j[l]]
                if temp not in matrix[k]:
                    flag = 1
            if flag==0:
                Slides.append(k)
                used[k] = True
                grandflag = 1
                break
        if grandflag==1:
            break

print(Slides)