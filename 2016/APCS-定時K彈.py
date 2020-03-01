# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 01:33:51 2020

@author: Eric
"""

try:
    N,M,K = list(map(int,input().split()))
    people = [x for x in range(1,N+1)]
    
    boom = -1
    for i in range(K):
        boom += M
        boom %= len(people)
        people.pop(boom)
        boom -= 1

    boom = (boom+1) % len(people)
    print(people[boom])
except EOFError:
    pass