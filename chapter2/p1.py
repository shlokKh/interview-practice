#Remove Dups write code to remove duplicates from an unsorted linked list

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

def remove_dups(head):
    h = set()
    
    curr = head
    prev = head
    while curr is not None:
        print("Prev: " + str(prev.data))
        print("Curr: " + str(curr.data))
        if curr.data in h:
            prev.next = curr.next
            curr = curr.next
            continue
        else:
            h.add(curr.data)
        
        prev = curr
        curr = curr.next
        print("-------------")
    print(h)
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.print_list()
head = remove_dups(head)
head.print_list()