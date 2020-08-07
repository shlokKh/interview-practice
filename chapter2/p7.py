#Find an intersection between two singly linked lists, determine if the two lists intserect return the intersecting node

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

def intersection(l1, l2):
    s = set()

    p1 = l1
    p2 = l2
    while p1 is not None or p2 is not None:
        if p1 is not None:
            if p1 in s:
                return p1
            else:
                s.add(p1)
            p1 = p1.next
        if p2 is not None:
            if p2 in s:
                return p2
            else:
                s.add(p2)
            p2 = p2.next

    return None

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
temp = l1.next.next
l2 = temp

print(intersection(l1, l2))

#Another way to do this is to iterate through both lists at the same time till you reach the last node and compare if they are the same
#Then do another iteration chopping off the length of the longer linked list and iterating through the same time until the pointers are the same
#Still O(n) and uses O(1) memory

