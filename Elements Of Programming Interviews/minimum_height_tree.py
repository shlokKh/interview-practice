class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

#Root should be constructed based on the middle of the array 
#basically a merge sort to find roots
def construct_min_height_bst(a):

    def construct_min_helper(start, end):
        if start >= end:
            return None
        middle = (start+end)//2
        return Node(a[middle], construct_min_helper(start, middle), construct_min_helper(middle+1, end))

    return construct_min_helper(0, len(a))
tree = construct_min_height_bst([1,2,3,5])

print(tree.val)
print(tree.left.val)
print(tree.right.val)
print(tree.left.left.val)
    