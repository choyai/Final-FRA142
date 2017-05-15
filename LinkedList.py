from Node import Node
class LinkedList:
    def __init__(self, size = None):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def add(self, node, pos):
        if self.size == 0:
            self.head = self.tail = node
            self.size = 1
        elif pos > self.size + 1:
            print("Error: List too small")
        elif pos < 0:
            print("you don't know how to count")
        else:
            if pos == 0:
                temp = self.head
                node.next = temp
                temp.previous = node
                self.head = node
                #print("adding head")
            elif pos == self.size:
                temp = self.tail
                temp.next = node
                node.previous = temp
                self.tail = node
                #print("adding tail")
                #print(temp)
            else:
                temp = Node()
                for i in range(pos - 1):
                    temp = self.head.next
                temp.previous.next = node
                node.previous = temp.previous
                temp.previous = node
                node.next = temp
                #print("adding pos "+ str(pos))
            self.size+=1
        #print("size = " + str(self.size))
        #print(self.head)
        #print(self.tail)

    def remove(self, pos):
        if pos >= self.size:
            print("list ain't that big, dumbass")
            return None
        else:
            if pos == 0:
                name = self.head.name
                self.head = self.head.next
                self.size -= 1
                return name
            elif pos == self.size - 1:
                name = self.tail.name
                self.tail = self.tail.previous
                self.size -= 1
                return name
            else:
                temp = self.head
                for i in range(pos - 1):
                    temp = temp.next
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.size -= 1
                return temp
    def report(self):
        temp = self.head
        while self.head is not None:
            print(temp)
            temp = temp.next