matrix = [[1,1,1,1,1,1,1,0,0,0],
[1,0,1,1,0,0,0,0,0,0],
[1,1,0,0,1,1,0,0,0,0],
[1,0,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1],
[0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,1,1,1],
[0,0,0,0,1,1,1,1,0,1],
[0,0,0,1,1,1,1,1,0,1]]

curr = [0,0,-1]
matrix[curr[0]][curr[1]] += 1
stack = []
np_flag = 0
nf = 0

while curr!=[9,9]:
    matrix[curr[0]][curr[1]] += 1
    cr = list(curr)
    cr[1]+=1
    cd = list(curr)
    cd[0] += 1
    if curr[1]>0:
        cl = list(curr)
        cl[1] -= 1
    if curr[0]>0:
        cu = list(curr)
        cu[0] -= 1

    if curr[2]==-1:
        if matrix[cr[0]][cr[1]]:
            curr[2] = 0
            stack.append(curr)
            curr = cr
        elif matrix[cd[0]][cd[1]]:
            curr[2] = 1
            stack.append(curr)
            curr = cd
        else:
            try:
                if matrix[cl[0]][cl[1]]:
                    curr[2] = 2
                    stack.append(curr)
                    curr = cl
            except:
                try:
                    if matrix[cu[0]][cu[1]]:
                        curr[2] = 3
                        stack.append(curr)
                        curr = cu
                except:
                    nf = 1
        if nf:
            try:
                curr = stack.pop()
            except:
                np_flag = 1
                break
    else:
        if curr[2] == 3:
            try:
                curr = stack.pop()
            except:
                np_flag = 1
                break

        if curr[2]==0:
            if matrix[cd[0]][cd[1]]:
                curr[2] = 1
                stack.append(curr)
                curr = cd
                break
            else:
                try:
                    if matrix[cl[0]][cl[1]]:
                        curr[2] = 2
                        stack.append(curr)
                        curr = cl
                except:
                    try:
                        if matrix[cu[0]][cu[1]]:
                            curr[2] = 3
                            stack.append(curr)
                            curr = cu
                    except:
                        try:
                            curr = stack.pop()
                        except:
                            np_flag = 1
                            break
        elif curr[2]==1:
            try:
                if matrix[cl[0]][cl[1]]:
                    curr[2] = 2
                    stack.append(curr)
                    curr = cl
            except:
                try:
                    if matrix[cu[0]][cu[1]]:
                        curr[2] = 3
                        stack.append(curr)
                        curr = cu
                except:
                    try:
                        curr = stack.pop()
                    except:
                        np_flag = 1
                        break
        elif curr[2]==2:
            try:
                if matrix[cu[0]][cu[1]]:
                    curr[2] = 3
                    stack.append(curr)
                    curr = cu
            except:
                try:
                    curr = stack.pop()
                except:
                    np_flag = 1
                    break

if np_flag:
    print("NO PATH")
else:
    print(matrix)