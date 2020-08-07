class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
def validateBST(root):
    lst = validate_bst_aux(root, [])
    prev = lst[0]
    for n in lst:
        if prev > n:
            return False
    return True

def validate_bst_aux(root, lst):
    if root is None:
        return lst
    validate_bst_aux(root.left, lst)
    lst.append(root.val)
    validate_bst_aux(root.right, lst)

    return lst

def check_bst(root):
    return check_bst_aux(root, None, None)

def check_bst_aux(root, min, max):
    if root is None:
        return True
    if min and root.val < min and max and root.val > max:
        return False
    
    return (check_bst_aux(root.left, min, root.val) or check_bst_aux(root.right, root.val, max))