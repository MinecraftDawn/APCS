# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:13:47 2020

@author: Eric
"""

try:
    while True:
        edges = list(map(int, input().split()))
        edges.sort()
        print(edges[0], edges[1], edges[2])
        if edges[0] + edges[1] <= edges[2]:
            print("No")
        else:
            a2 = edges[0]*edges[0]
            b2 = edges[1]*edges[1]
            c2 = edges[2]*edges[2]
            
            if a2 + b2 < c2:
                print("Obtuse")
            elif a2 + b2 == c2:
                print("Right")
            else:
                print("Acute")
except EOFError:
    pass
