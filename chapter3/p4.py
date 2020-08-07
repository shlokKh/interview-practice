class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def pop_all(self):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

    def push(self, x):
        self.s1.append(x)
    
    def pop(self):
        if len(self.s2) == 0:
            self.pop_all()
        
        return self.s2.pop()




q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())