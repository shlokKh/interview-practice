from collections import defaultdict
from queue import Queue
def numConnectedComponents(edges, n):
    graph = defaultdict(lambda: set())
    def buildGraph():
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
    buildGraph()
    
    def dfs():
        visited = set()
        stack = []
        components = 0
        for i in range(n):
            if i not in visited:
                stack.append(i)
                components += 1
            while stack:
                node = stack.pop()
                visited.add(node)
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    
        return components
    
    return dfs()

print(numConnectedComponents([[0, 1], [1, 2], [2, 3], [3, 4]], 5))
            

