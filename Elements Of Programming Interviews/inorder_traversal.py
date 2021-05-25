
def inorder_traversal(root):
    prev, result = None, []

    while root:
        if root.parent is prev:
            if root.left:
                next = root.left
            else:
                result.append(root.data)
                if root.right:
                    next = root.right
                else:
                    next = root.parent
        elif root.left is prev:
            result.append(root.data)
            if root.right:
                next = root.right
            else:
                next = root.parent
        else:
            next = root.parent
        prev, root = root, next
    return result

def preorder_traversal(root):
    prev, result = None, []

    while root:
        if root.parent is prev:
            result.append(root.data)
            next = root.left or root.right or root.parent
        elif root.left is prev:
            next = root.right or root.parent
        else:
            next = root.parent

        prev, root = root, next
    return result

def postorder_traversal(root):
    prev, result = None, []
    while root:
        if root.parent is prev:
            result.append(root.data)
            next = root.right or root.left or root.parent
        elif root.right is prev:
            next = root.left or root.parent
        else:
            next = root.parent

        prev, root = root, next
    result.reverse()
    return result


        

class Node():
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

root = Node(1)
root.left = Node(2)
root.left.parent = root
root.right = Node(3)
root.right.parent = root
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.parent = root.left
root.left.right.parent = root.left

print(inorder_traversal(root))
print(preorder_traversal(root))
print(postorder_traversal(root))