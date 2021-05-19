from typing import List
from collections import defaultdict
def alienDictionary(orderedDictionary: List[str]):
    indegrees = {}
    graph = defaultdict(lambda: set())
    def buildGraph():
        for i in range(len(orderedDictionary)-1):
            w1 = orderedDictionary[i]
            w2 = orderedDictionary[i+1]
            idx = 0
            while w1[idx] == w2[idx]:
                if w1[idx] not in indegrees:
                    indegrees[w1[idx]] = 0
                idx += 1
            
            graph[w1[idx]].add(w2[idx]) 
            if w2[idx] not in indegrees:
                indegrees[w2[idx]] = 0
            if w1[idx] not in indegrees:
                indegrees[w1[idx]] = 0
            indegrees[w2[idx]] += 1

    def topSort():
        queue = []
        order = []
        for n in indegrees:
            if indegrees[n] == 0:
                queue.append(n)

        while queue:
            node = queue.pop(0)
            order.append(node)
            for edge in graph[node]:
                indegrees[edge] -= 1

                if indegrees[edge] == 0:
                    queue.append(edge)
        return order


    buildGraph()
    print(indegrees)
    print(graph)
    order = topSort()
    return order if len(order) == len(indegrees) else []

print(alienDictionary([
"z", "a", "z"
]))
