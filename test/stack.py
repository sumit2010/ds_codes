class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            _, till_min = self.stack[-1]
            self.stack.append((x, min(till_min, x)))
        else:
            self.stack.append((x, x))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def print_stack(self):
        print self.stack

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        if self.s1.is_empty():
            self.front_elt = x
        self.s1.push(x)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        self.s2.pop()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def front(self):
        if self.s2.is_empty():
            return self.s2.peek()
        return self.front_elt


q = Queue()
q.enqueue(1)
q.enqueue(2)

print q.front()
q.dequeue()
print q.front()
