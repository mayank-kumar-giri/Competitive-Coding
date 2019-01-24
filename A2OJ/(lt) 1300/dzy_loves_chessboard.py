n,m = map(int, input().split())
arr = []
d = {'.':0,'-':1,'B':2,'W':3}
rd = {0:'.',1:'-',2:'B',3:'W'}

for i in range(n):
    temp = input()
    t = []
    for j in temp:
        t.append(d[j])
    arr.append(t)

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            arr[i][j]=rd[1]
        elif arr[i][j]==0:
            if i==0 and j==0:
                arr[i][j]=rd[2]
            else:
                if arr[i][j-1]=='B' or arr[i-1][j]=='B':
                    arr[i][j] = rd[3]
                else:
                    arr[i][j] = rd[2]

for i in range(n):
    for j in range(m):
        print(arr[i][j],end='')
    print('')