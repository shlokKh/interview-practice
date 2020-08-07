class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def push(self,x):
        self.size += 1
        self.stack.append(x)
    
    def peek(self):
        return self.stack[self.size-1]
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def print_stack(self):
        print(self.stack)

def sort_stacks(stack):
    sorted_stack = Stack()
    min_num = 100000

    while not stack.isEmpty():
        temp = stack.pop()
        while not sorted_stack.isEmpty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    
    while not sorted_stack.isEmpty():
        stack.push(sorted_stack.pop())
    
    return stack
        

s = Stack()
s.push(5)
s.push(7)
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
sort_stacks(s).print_stack()
    