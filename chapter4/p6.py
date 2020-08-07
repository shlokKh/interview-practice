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


def in_order_successor(node):
    if node is None:
        return None
    elif node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp
    else:
        temp = node.parent
        while temp and temp.left != node:
            node = temp
            temp = node.parent
        return temp