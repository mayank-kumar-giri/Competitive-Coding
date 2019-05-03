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
# print(photos)
for i in range(len(photos)):
    photos[i] = list(photos[i].split(" "))

interest = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        a = set()
        b = set()
        for k in photos[i][2:]:
            a.add(k)
        for k in photos[j][2:]:
            b.add(k)
        # print(a,b)
        i1 = len(list(a-b))
        i2 = len(list(a & b))
        i3 = len(list(b-a))
        # print(i1,i2,i3)
        interest[i][j] = min(i1,i2,i3)
        # print(interest)
# print(interest)
