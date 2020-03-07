class Node:
    def __init__(self, value:int):
        self.value = value
        self.childs = []
        self.height = 0
        
nodeCount = int(input())
nodes = {}
for i in range(1, nodeCount+1):
    node = Node(i)
    nodes[i] = node
    
for i in range(1, nodeCount+1):
    for num in list(map(int, input().split()))[1:]:
        nodes[i].childs.append(nodes[num])
    
visted = set()

def dfs(node:Node):
    if not node.childs:
        return node.height
    
    if node in visted:
        return node.height
    
    for child in node.childs:
        node.height = max(node.height, dfs(child)+1)
        
    visted.add(node)
    return node.height
    

for node in nodes.values():
    dfs(node)

root = (0, 0)
sumHeight = 0
for k,node in nodes.items():
    root = max(root, (node.height, k))
    sumHeight += node.height

print(root[1])
print(sumHeight)