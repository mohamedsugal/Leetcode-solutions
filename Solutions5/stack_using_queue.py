class Stack:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue
        # [3,2,1]

    def dequeue(self):
        queue_helper = []
        while len(self.queue) != 1:
            x = self.queue.pop()
            queue_helper.append(x)
        temp = self.queue.pop()
        while queue_helper:
            x = queue_helper.pop()
            self.queue.append(x)
        return temp


stack = Stack()
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)

print(stack.dequeue())

