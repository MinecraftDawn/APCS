# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:57:22 2020

@author: Eric
"""

try:
    N,M = list(map(int, input().split()))
    selected = []
    for _ in range(N):
        row = list(map(int, input().split()))
        selected.append(max(row))
        
    total = sum(selected)
    print(total)
    
    div = []
    for item in selected:
        if total % item == 0:
            div.append(item)
    
    if div:       
        print(" ".join(str(x) for x in div))
    else:
        print(-1)
    
except EOFError:
    pass