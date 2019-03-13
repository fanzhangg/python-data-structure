class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def peek(self):
        return self.items[-1]

    def pop(self):
        if self.isempty():
            raise IndexError("pop from empty list")
        i = self.peek()
        self.items = self.items[0: -1]
        return i

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items == []
