#Return Kth to Last element

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

def kth_last(head, k):
    if k < 0:
        return None
    size = 0
    curr = head
    while curr is not None:
        curr = curr.next
        size += 1
    
    iterate = size - k
    curr = head

    for i in range(iterate-1):
        curr = curr.next
    
    return curr


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.print_list()
head = kth_last(head, 4)
head.print_list()