# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 21:30:02 2020

@author: Eric
"""
points = {"1":1,
          "2":2,
          "3":3,
          "H":4}


try:
    player = []
    for _ in range(9):
        tmp = input().split()
        player.append(tmp[1:])
        
    out = int(input())
    
    hits = []
    done = False
    while not done:
        for i in range(9):
            if player[i]:
                hits.append(player[i].pop(0))
            else:
                done = True
    
    ans = 0
    outNum = 0
    baseBag = [False] * 4
    while outNum < out:
        cur = hits.pop(0)[0]
        if cur in points:
            step = points[cur]
            baseBag[0] = True
            for i in range(3,-1,-1):
                if baseBag[i]:
                    if i + step > 3:
                        ans += 1
                    else:
                        baseBag[i + step] = True
                    baseBag[i] = False
        else:
            outNum += 1
            if outNum % 3 == 0:
                baseBag = [False] * 4
    
    print(ans)
except EOFError:
    pass
