from pyllist import sllist
class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)

def list_of_depths(t):
    queue = []
    depths = []
    
    queue.append(t)
    print(queue)
    while len(queue) != 0:
        ll = sllist()
        aux = []
        while len(queue) != 0:
            node = queue.pop(0)
            ll.append(node)
            if node.left:
                aux.append(node.left)
            if node.right:
                aux.append(node.right)
        
        queue = aux
        depths.append(ll)
    
    return depths

def minimal_tree(l):
    length = len(l)
    mid = length // 2
    t = Node(l[mid])
    return minimal_tree_aux(t, l)

def minimal_tree_aux(node, l):
    if l is None:
        return node
    if len(l) == 1:
        return node
    left = l[:(len(l)//2)]
    right = l[(len(l)//2+1):]
    if len(left) != 0:
        node.left = Node(left[len(left)//2])
        node.left = minimal_tree_aux(node.left, left)
    if len(right) != 0:
        node.right = Node(right[len(right)//2])
        node.right = minimal_tree_aux(node.right, right)
    return node


t = minimal_tree([1,2,3,4,5,6,7,8,9,10])

depth = list_of_depths(t)
for d in depth:
    print(d)



        


