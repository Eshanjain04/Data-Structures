class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]

    def peek(self):
        return self.queue[0]

    def printQueue(self):
        for i in self.queue:
            print(i,end=' ')

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.dequeue()
queue.printQueue()

