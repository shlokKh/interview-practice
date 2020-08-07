#palindrome
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

def palindrome(l):
    p1 = l
    p2 = l
    stack = []
    size = 0
    while p1 is not None:
        stack.append(p2.data)
        p2 = p2.next
        p1 = p1.next
        size += 1
        if p1 is not None:
            size += 1
            p1 = p1.next
        
    if size % 2 == 1:
        p2 = p2.next
    
    while p2 is not None:
        if stack.pop() != p2.data:
            return False
        p2 = p2.next
    
    return True

l1 = ListNode(9)
l1.next = ListNode(1)
l1.next.next = ListNode(1)
l1.next.next = ListNode(9)
print(palindrome(l1))
