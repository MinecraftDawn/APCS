try:
    while True:
        R, C, M = list(map(int, input().split()))
        
        matrix = []
        for _ in range(R):
            matrix.append(list(map(int, input().split())))
            
        oper = list(map(int,input().split()))
        
        def matrixOper(matrix:list, oper:int):
            if oper == 0:
                return list(zip(*matrix))[::-1]
            else:
                return matrix[::-1]
        
        for o in oper[::-1]:
            matrix = matrixOper(matrix, o)
        
        print(len(matrix), len(matrix[0]))
        for row in matrix:
            print(" ".join(map(str,row)))
except EOFError:
    pass