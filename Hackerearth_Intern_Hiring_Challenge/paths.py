class TreeNode:
   def __init__(self, x):
       self.val = x
       self.children = []

root = TreeNode(0)

n,k = map(int, input().split())
edges = []
nodes = []
for i in range(n-1):
    edges.append(list(map(int, input().split())))
    if i==0:
        nodes.append(TreeNode(edges[-1][0]))
        nodes.append(TreeNode(edges[-1][1]))
        nodes[-2].children.append(nodes[-1])
    if edges[-1][1] not in nodes:
        nodes.append(edges[-1][1])



