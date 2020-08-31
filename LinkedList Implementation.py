class Node():
    def __init__(self,data):
        self.data=data
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.head=None
        self.size = 0

    def insertBeginning(self,data):
        self.size+=1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode=self.head
            self.head = newNode

    def insertEnd(self,data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self,data):
        self.size-=1
        currentNode = self.head
        previousNode = None
        while currentNode.data!=data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def size1(self):
        return self.size

    def printList(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode


linked = LinkedList()
linked.insertBeginning(21)
linked.insertBeginning(24)
linked.insertEnd(56)
linked.insertEnd(3)
linked.insertBeginning(30)
linked.insertEnd(5)
linked.printList()
linked.remove(24)
linked.printList()
print(linked.size1())


