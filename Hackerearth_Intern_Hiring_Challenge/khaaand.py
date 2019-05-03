n,k = list(map(int,input().split()))
tree_adj_list = {}


for i in range(n-1):
    u,v = list(map(int,input().split()))
    try:
        tree_adj_list[u].append(v)
    except:
        tree_adj_list[u] = [v]
    try:
        tree_adj_list[v].append(u)
    except:
        tree_adj_list[v] = [u]


ltk = []


for i in tree_adj_list.keys():
    if i<k:
        ltk.append(i)
    else:
        tp = []
        for j in range(len(tree_adj_list[i])):
            if tree_adj_list[i][j]>=k:
                tp.append(tree_adj_list[i][j])
        tree_adj_list[i] = tp
for i in ltk:
    del tree_adj_list[i]


dfsstack = []
not_yet_visited = set(tree_adj_list.keys())
final_answer = []

while len(not_yet_visited)!=0:
    start = list(not_yet_visited)[0]
    dfsstack.append(start)
    tp_set = set()
    while dfsstack!=[]:
        curr = dfsstack.pop()
        if curr in not_yet_visited:
            dfsstack.extend(tree_adj_list[curr])
            tp_set.add(curr)
            not_yet_visited.remove(curr)
    final_answer.append(tp_set)


ans = 0
for i in range(len(final_answer)):
    n = len(final_answer[i])
    ans += n*(n-1) / 2
print(int(ans))