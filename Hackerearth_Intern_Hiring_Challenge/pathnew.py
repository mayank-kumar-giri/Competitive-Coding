n,k = map(int, input().split())
tree = {}
nodes = []
for i in range(n-1):
    a,b = map(int, input().split())

    if a not in nodes:
        nodes.append(a)
    if b not in nodes:
        nodes.append(b)

    if a not in tree.keys():
        tree[a] = [b]
    else:
        tree[a].append(b)


count = 0
# print(nodes)
for i in nodes:
    if i not in tree.keys():
        continue
    stack = []
    root = i
    min_in_currpath = root
    stack.append([root,min_in_currpath])

    while stack:
        curr,min_in_currpath = stack.pop()
        # print(curr,min_in_currpath,stack)
        if curr != root:
            if min_in_currpath>=k:
                count+=1

        if min_in_currpath>=curr:
            min_in_currpath = curr

        if curr not in tree.keys():
            pass
        else:
            temp = min_in_currpath
            for i in tree[curr]:
                if temp>=i:
                    temp = i
                stack.append([i,temp])
    # print(count, min_in_currpath, stack)

print(count)