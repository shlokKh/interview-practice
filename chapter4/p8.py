class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.Right = None

#r = root, v1 = val1, v2 = val2
def first_common_ancestor(r, v1, v2):
    if not covers(r, v1) or not covers(r, v2):
        return None

    return first_common_ancestor_aux(r, v1, v2)

def first_common_ancestor_aux(r, v1, v2):
    if not r or v1 == r or v2 == r:
        return r
    
    v1IsOnLeft = covers(r.left, v1)
    v2IsOnLeft = covers(r.left, v2)

    if v1IsOnLeft != v2IsOnLeft:
        return r
    temp = r.left if v1IsOnLeft else r.right
    return first_common_ancestor_aux(temp, v1, v2)
    
def covers(r, v1):
    if r == None:
        return False
    if r == v1:
        return True
    
    return covers(r.left, v1) or covers(r.right, v1)