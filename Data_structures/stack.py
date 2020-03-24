class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def isEmpty(self):
        return self.items == []