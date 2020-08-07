#loop Detection

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
#First step is to find a loop
#This can be done having a pointer that moves twice as fast as another pointer and check when they collide
def loop_detection(l):
    slow = l
    fast = l
    count = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        print("Iteration " + str(count))
        print("Slow: " + str(slow.data))
        print("Fast: " + str(fast.data))
        print("")
        if slow == fast:
            break 
        count += 1

    slow =  l
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow



l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = l1

print(loop_detection(l1).data)