class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def printStack(self):
        for i in self.stack:
            print(i)

stack = Stack()
stack.push(20)
stack.push(30)
stack.push(10)
stack.push(50)
#stack.printStack()
stack.pop()
stack.printStack()