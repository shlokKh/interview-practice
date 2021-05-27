'''
Not possible for an inorder traversal many combinations of a tree from just a few nodes
'''

def pre_order_construction(traversal):
    
    root_idx = [0]
    def pre_order_helper(lower_bound, upper_bound):
        if root_idx[0] == len(traversal):
            return None
        root = traversal[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        left = pre_order_helper(lower_bound, root)
        right = pre_order_helper(root, upper_bound)

        return TreeNode(root, left, right)

    
    return pre_order_helper(float('-inf'), float('inf'))