class Node:
    def __init__(self, value:int):
        self.value = value
        self.dad = None
        self.childs = []
        self.height = 0

nodeCount = int(input())
nodes = {}
queue = []
for i in range(1, nodeCount+1):
    node = Node(i)
    nodes[i] = node

for i in range(1, nodeCount+1):
    childs = list(map(int, input().split()))[1:]
    if not childs:
        queue.append(nodes[i])
        
    for num in childs:
        nodes[i].childs.append(nodes[num])
        nodes[num].dad = nodes[i]
        
#for k,v in nodes.items():
#    print(v.dad)

while queue:
    node = queue.pop(0)
    if not node.dad:
        break
    node.dad.childs.remove(node)
    node.dad.height = max(node.dad.height, node.height+1)
    if not node.dad.childs:
        queue.append(node.dad)

sumHeight = 0
for v in nodes.values():
    sumHeight += v.height
    
print(node.value)
print(sumHeight)