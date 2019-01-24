arr = []
new_arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
    new_arr.append([0,0,0])

def total(arr,i,j):
    valid = list(range(3))
    ans = arr[i][j]
    if (i + 1) in valid:
        ans += arr[i + 1][j]
    if (j + 1) in valid:
        ans += arr[i][j + 1]
    if (i - 1) in valid:
        ans += arr[i - 1][j]
    if (j - 1) in valid:
        ans += arr[i][j - 1]
    return ans

for i in range(3):
    for j in range(3):
        new_arr[i][j] = total(arr,i,j)

# print(new_arr)

for i in range(3):
    for j in range(3):
        if (new_arr[i][j]%2)==0:
            new_arr[i][j] = 1
        else:
            new_arr[i][j] = 0
        print(new_arr[i][j],end='')
    print('')