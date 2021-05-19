from collections import defaultdict
from queue import Queue
def validTree(edges, n):
    graph = defaultdict(lambda: set())

    def buildGraph():
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

    def detectCycle():
        queue = Queue()
        visited = set()
        queue.put((0, None))
        
        while not queue.empty():
            node, prev = queue.get()
            visited.add(node)
            for edge in graph[node]:
                if edge in visited and edge != prev:
                    return True
                if edge not in visited:
                    queue.put((edge, node))

        return False if len(visited) == n else True


            
    
    buildGraph()
    return not detectCycle()

def validTreeDisjointSet(edges, n):
    graph = defaultdict(lambda: set())
    def find_parent(parent, i):
        if parent[i] == -1:
            return i
        return find_parent(parent, parent[i])

    def union(parent, x, y):
        x_set = find_parent(parent, x)
        y_set = find_parent(parent, y)
        parent[x_set] = y_set

    def findCycle():
        parents = [-1]*n
        for v, e in edges:
            x = find_parent(parents, v)
            y = find_parent(parents, e)
            if x == y:
                return True
            union(parents, x, y)

        return -1 in parents[:-1]

    return not findCycle()

print(validTreeDisjointSet([[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 5))