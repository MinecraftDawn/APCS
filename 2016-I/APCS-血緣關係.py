try:
    while True:
        count = int(input())
        
        nodes = [[] for _ in range(count)] 
        
        root = count * (count-1) // 2
        for _ in range(count-1):
            dad, son = map(int, input().split())
            nodes[dad].append(son)
            root -= son
        
        ans = 0
        def dfs(node):
            maxPath,secondPath = 0,0
            for child in nodes[node]:
                path = dfs(child)
                if path >= maxPath:
                    maxPath,secondPath = path, maxPath
                elif path > secondPath:
                    secondPath = path
            
            global ans
            ans = max(ans, maxPath+secondPath)  
              
            return maxPath + 1
        
        dfs(root)
        
        print(ans)
except EOFError:
    pass