class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # could just use return self.items.pop()
        popped = self.items[-1]
        self.items = self.items[:-1]
        return popped

    def peek(self):
        return self.items[-1]
        
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.primary = Stack()
        self.secondary = Stack()

    def enqueue(self, item):
        if not self.primary.isEmpty():
            self.primary.push(item)
        else:
            while not self.secondary.isEmpty():
                self.primary.push(self.secondary.pop())
            self.primary.push(item)
    def dequeue(self):
        if not self.secondary.isEmpty():
            return self.secondary.pop()
        else:
            while not self.primary.isEmpty():
                self.secondary.push(self.primary.pop())
            return self.secondary.pop()

        # while not self.primary.isEmpty():
        #     self.secondary.push(self.primary.pop())
        # popped = self.secondary.pop()
        # while not self.secondary.isEmpty():
        #     self.primary.push(self.secondary.pop())
        # return popped

    def isEmpty(self):
        return self.primary.items == [] and self.secondary.items == []

    def size(self):
        return len(self.primary.items) + len(self.secondary.items)

test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.enqueue(4)
#print test.primary.items
test.dequeue()
test.dequeue()
#print test.primary.items


