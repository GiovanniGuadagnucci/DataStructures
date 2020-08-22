class Node (object):
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None

    def addNode(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = Node(data)

    def addHeadNode(self,data):
        head = self.head
        self.head = Node(data)
        self.head.next = head
        del head

    def addBetwinNode(self, data ,location):
        newNode = Node(data)
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == location:
                previusNode.next = newNode
                newNode.next = currentNode
                break
            previusNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1



    def print(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

list1 = linked_list()
list1.addNode(2)
list1.addNode(1)
list1.addNode(3)
list1.addNode(10)
list1.addNode(12)
list1.addBetwinNode(5,1)
list1.addHeadNode(20)
list1.print()
