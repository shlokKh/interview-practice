class Graph:
    def __init__(self):
        self.graph = {}
        self.map = {}
        self.num_nodes = 0
        self.num_edges = 0
    
    def add_node(self, name):
        self.map[name] = Project(name)
        self.graph[self.map[name]] = []
        self.num_nodes += 1

    def remove_node(self, name):
        self.graph.pop(self.map[name])

    def add_edge(self, src, dest):
        self.graph[self.map[src]].append(self.map[dest])
        self.map[dest].dependencies += 1 
        self.num_edges += 1

    def remove_edge(self, src, dest):
        self.graph[self.map[src]].remove(self.map[dest])
        self.map[dest].dependencies -= 1 
        self.num_edges -= 1

    def get_num_edges(self):
        return self.num_edges

    def find_0_incoming_edges(self):
        e = []
        for k,_ in self.graph.items():
            if k.dependencies == 0:
                e.append(k.name)
        
        return e
    
    def print_graph(self):
        for nodes in self.graph:
            print("Node: " + str(nodes))
            for e in self.graph[nodes]:
                print("Edges: " + str(e) + ", ")
            print("----------------")
class Project:
    def __init__(self, name):
        self.name = name
        self.dependencies = 0
        self.map = {}
    
    def __str__(self):
        return self.name + " " + str(self.dependencies)
    
def build_order(projects, dependencies):
    g = Graph()
    build_order = []
    for p in projects:
        g.add_node(p)

    for d, s in dependencies:
        g.add_edge(d, s)

    count = 0
    g.print_graph()
    nodes = g.find_0_incoming_edges()
    while count < len(projects):
        curr = nodes[0]
        print(curr)
        if not curr:
            return None
        
        build_order.append(curr)
        print(len(g.graph[g.map[curr]]))
        temp = []
        for e in g.graph[g.map[curr]]:
            temp.append(e)
            print("Removing edge: " + e.name)
        for e in temp:
            g.remove_edge(curr, e.name)
        g.remove_node(curr)
        count += 1
        g.print_graph()
        nodes = g.find_0_incoming_edges()

    return build_order
        
        

        
        





# def top_sort_aux(g, v, visited, stack):
#     visited[v] = True

#     for i in g.graph[v]:
#         if visited[i] == False:
#             top_sort_aux(g, i, visited, stack)
    
#     stack.insert(0,v)

# def top_sort(g, projects):
#     visited = {}
#     stack = []
#     for p in projects:
#         visited[p] = False
#     for p in projects:
#         if visited[p] == False:
#             top_sort_aux(g, p, visited, stack)

#     return stack






projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

print(build_order(projects, dependencies))