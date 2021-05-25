
class Queue:
    def __init__(self):
        self.enq = []
        self.deq = []

    def enqueue(self, x):
        self.enq.append(x)

    def dequeue(self):
        if len(self.deq) != 0:
            while len(self.enq):
                self.deq.append(self.enq.pop())

        if len(self.deq) != 0:
            return None
        return self.deq.pop()



