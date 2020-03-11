from functools import cmp_to_key

count = int(input())
weight = list(map(int, input().split()))
use = list(map(int, input().split()))

class Item:
    def __init__(self, weight:int, useTime:int):
        self.weight = weight
        self.useTime = useTime
        
items = []        
for i in range(count):
    items.append(Item(weight[i], use[i]))

def cmp(item1:Item, item2:Item):
    if item1.useTime*item2.weight > item2.useTime*item1.weight:
        return -1
    else:
        return 1

items.sort(key=cmp_to_key(cmp))

cost = 0
sumWeight = 0
for item in items:
    cost += sumWeight*item.useTime
    sumWeight += item.weight

print(cost)   