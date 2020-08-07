class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

    def print_list(self):
        curr = self
        s = ""
        while curr is not None:
            s += str(curr.data) + "-> "
            curr = curr.next
        print(s)

def partition(head, partition):
    l1 = []
    l2 = []
    curr = head
    while curr is not None:
        if curr.data < partition:
            l1.append(curr.data)
        else:
            l2.append(curr.data)

    curr = None
    l = l1 + l2
    for i in l:
        curr = ListNode(i)
        curr = curr.next
    
    return curr
        