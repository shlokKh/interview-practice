class StackOfPlates:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [[]]
        self.c = 0
        self.size = 0
    
    def push(self, x):
        stack = self.stacks[self.c]
        if len(stack) == 0:
            stack.append(x)
        elif len(stack) == self.threshold:
            self.c += 1
            self.stacks.append([x])
        else:
            stack.append(x)
        
        self.size += 1
    
    def pop(self):
        stack = self.stacks[self.c]
        if len(stack) == 1:
            val = stack.pop()
            self.stacks.pop()
            self.c -= 1
            self.size -= 1
            return val
        else:
            val = stack.pop()
            self.size -= 1
            return val

    def print_contents(self):
        for s in self.stacks:
            print("Stack: ")
            print(s)
            print("")

s = StackOfPlates(3)
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.print_contents()
print(s.push(3))
print(s.pop())
print(s.pop())
