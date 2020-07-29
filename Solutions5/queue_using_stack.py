class Queue:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        helper_stack = []
        while len(self.stack) != 1:
            x = self.stack.pop()
            helper_stack.append(x)
        temp = self.stack.pop()
        while helper_stack:
            x = helper_stack.pop()
            self.stack.append(x)
        return temp
    

q = Queue()
q.push(9)
q.push(5)
q.push(3)

print(q.pop())
print(q.pop())