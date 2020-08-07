#Sum List
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

def sum_list(l1, l2):
    place = 0
    carry = 0
    c1 = l1
    c2 = l2
    total = 0
    while c1 is not None or c2 is not None:
        temp = 0
        if c1 is not None:
            temp += c1.data
            c1 = c1.next
        if c2 is not None:
            temp += c2.data
            c2 = c2.next
        if carry == 1:
            temp += carry
            carry = 0

        if temp >= 10:
            temp -= 10
            carry = 1
        total += temp*(10**place)
        place += 1

    total += carry*(10**place)
    
    return total

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(1)

print(sum_list(l1, l2))
