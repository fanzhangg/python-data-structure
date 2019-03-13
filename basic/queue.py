class Queue:
    def __init__(self):
        self.items = []

    def put(self, i):
        self.items.insert(0, i)

    def get(self, i):
        self.items.pop()

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)
