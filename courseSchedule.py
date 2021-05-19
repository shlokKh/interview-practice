'''
Detect a cycle in the graph. This can be done by building a graph out
then by using DFS to determine if there is a back edge. If there isn't return true
and if there is return FALSE
'''
from collections import defaultdict
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    def buildGraph():
        graph = defaultdict(lambda: set())
        indegree = [0]*numCourses
        for e in prerequisites:
            graph[e[0]].add(e[1])
            indegree[e[1]] += 1
        return graph, indegree
    
    
    def topSort(graph, indegree):
        queue = []
        count = 0
        for i in range(numCourses): 
            if indegree[i] == 0: 
                queue.append(i) 
        
        while queue:
            u = queue.pop(0)
            
            for i in graph[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            count += 1
        
        if count != numCourses:
            return False
        
        return True
        
    
    graph, indegree = buildGraph()
    
    return topSort(graph, indegree)
        
print(canFinish(2, [[1,0], [0, 1]]))