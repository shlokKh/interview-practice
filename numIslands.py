from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if not grid: return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m = len(grid)
    n = len(grid[0])
    
    def dfs(i, j):
        grid[i][j] = "0"
        for d1, d2 in directions:
            x, y = d1+i, d2+j
                
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                continue
            
            dfs(x, y)
    numIslands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                numIslands += 1
                dfs(i, j)
    
    return numIslands
        
        
        
        
        
        