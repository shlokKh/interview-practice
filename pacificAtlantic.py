from typing import List 

def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix: return []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    results = []
    m = len(matrix)
    n = len(matrix[0])
    pacificVals = [[False]*n for _ in range(m)]
    atlanticVals =  [[False]*n for _ in range(m)]
    
    def dfs(i, j, visited):
        visited[i][j] = True
        
        for x, y in directions:
            n_i, n_j = i+x, j+y
            
            if n_i >= m or n_i < 0 or n_j >= n or n_j < 0 or matrix[n_i][n_j] > matrix[i][j]:
                continue
            
            dfs(n_i, n_j, visited)
    
    for i in range(m):
        dfs(i, 0, pacificVals)
        dfs(i, n-1, atlanticVals)
    for j in range(n):
        dfs(0, j, pacificVals)
        dfs(m-1, j, atlanticVals)
    
    for i in range(m):
        for j in range(n):
            if pacificVals[i][j] and atlanticVals[i][j]:
                results.append([i, j])
    
    return results


pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])