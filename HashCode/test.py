tags = set()
fo = open("a_example.txt","r")
photos = []
for i in fo:
    photos.append(i)
photos = [photos[0]]+[photos[1]]+[photos[2]+photos[3]]+[photos[4]]
photos[2] = "H 3 selfie smile garden\n"
# print(photos)

for i in range(len(photos)):
    x = len(photos[i])
    photos[i] = photos[i][:x-1]
n = int(photos[0])
n = n-1
photos = photos[1:]

for i in range(len(photos)):
    photos[i] = list(photos[i].split(" "))
    for j in range(2,len(photos[i])):
        tags.add(photos[i][j])
tags = list(tags)
t = len(tags)
print(tags)
matrix = [[False for x in range(t)] for y in range(n)]
print(photos)

for i in range(n):
    for j in range(t):
        if tags[j] in photos[i]:
            matrix[i][j] = True

print(matrix)

from itertools import combinations

Slides = []
Slides.append(0)
used = [False]*n
used[0] = True

for i in range(n):
    if i!=0:
        if used[i]:
            continue
        else:
            Slides.append(i)
            used[i]=True

    present = []
    for j in range(len(matrix[i])):
        if matrix[i][j]:
            present.append(j)
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
                if matrix[k][j[l]]==False:
                    flag = 1
            if flag==0:
                Slides.append(k)
                used[k] = True
                grandflag = 1
                break
        if grandflag==1:
            break

print(Slides)