t = int(input())
for i in range(t):
    n = int(input())
    dishes = []
    for j in range(n):
        dishes.append(input().strip())
    count = 0
    vowels = {"a":16,"e":8,"i":4,"o":2,"u":1}
    ans = []
    for j in range(len(dishes)-1):
        for k in range(j+1,len(dishes)):
            s1 = 0
            s2 = 0
            for l in dishes[j]:
                s1 = s1 | vowels[l]
            for l in dishes[k]:
                s2 = s2 | vowels[l]
            if (s1 | s2)==31:
                count+=1
                print(s1,s2,(s1 | s2)==31)
                if [s1,s2] not in ans:
                    ans.append([s1,s2])
                    ans.append([s2,s1])
    print(count)
    for j in ans:
        print(j[0],j[1])