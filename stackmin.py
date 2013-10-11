class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        popped = self.items[-1]
        self.items = self.items[:-1]
        return popped

    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)

class StackMin:
    def __init__(self):
        self.stack = Stack()
        self.min_tracker = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.min_tracker.isEmpty():
            self.min_tracker.push(item)
        elif item < self.min_tracker.peek():
            self.min_tracker.push(item)
        else:
            self.min_tracker.push(self.min_tracker.peek())

    def get_min(self):
        return self.min_tracker.peek()

    def pop(self):
        self.min_tracker.pop()
        return self.stack.pop()

test = StackMin()
test.push(10)
test.push(5)
test.push(7)
test.push(3)
test.push(8)
test.push(1)
test.push(6)
test.push(9)

while test.stack.size() > 1:
    test.pop()
    print test.get_min()








