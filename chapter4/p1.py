class Graph:
    def __init__(self):
        self.nodes = []
        self.count = 0
    
    def add_vertex(self):
        new_node = Node(self.count)
        self.nodes.append(new_node)
        self.count += 1

    def add_edge(self, src, dest):
        self.nodes[src].add_child(dest)




class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
    
    def add_child(self, id):
        self.children.append(Node(id))



def route_between(g, src, dest):
    visited = set()
    return searchAux(g, src, dest, visited)

def searchAux(g, src, dest, visited):
    visited.add(g.nodes[src])
    children = g.nodes[src].children
    for c in children:
        if c.id == dest:
            return True
        if c not in visited:
            return searchAux(g, c.id, dest, visited)

    return False
            






g = Graph()
g.add_vertex()
g.add_vertex()
g.add_vertex()
g.add_vertex()

g.add_edge(1,2)

print(route_between(g,1,3))