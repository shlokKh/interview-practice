def lca(n1, n2):
    visited = set()

    while n1 or n2:
        if n1 in visited or n2 in visited:
            return n1 if n1 in visited else n2
        if n1:
            visited.add(n1)
            n1 = n1.parent
        if n2:
            visited.add(n2)
            n2 = n2.parent
    
    return None
