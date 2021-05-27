class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

'''
l1 -> (2, 4, 6)
l2 -> (3, 5, 7)
'''

def merge_linked_lists(l1, l2):    
    dummy_node = Node(0)
    curr = dummy_node
    while l1 and l2:
        if l1.val <  l2.val:
            curr.next = l1
            l1 = l1.next
            curr.next.next = None
        else:
            curr.next = l2
            l2 = l2.next
            curr.next.next = None
        curr = curr.next
    
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy_node.next

'''
Goal is to split linked list in half and merge and sort

'''
def sort_linked_list(l):
    if not l:
        return []
    fast_pointer = l
    slow_pointer = l
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
    
    l1 = l
    l2 = slow_pointer.next
    slow_pointer.next = None

    return merge_linked_lists(sort_linked_list(l1), sort_linked_list(l2))





