from LinkedList import LinkedList
class Queue(LinkedList):
    def __init__(self, size = 0):
        LinkedList.__init__(self, size = None)
    def isEmpty(self):
        return LinkedList.isEmpty()
    def add(self, node):
        LinkedList.add(self, node, self.size)
    def remove(self):
        if self.size != 0:
            name = self.head.name
            self.head = self.head.next
            self.size -= 1
            return name
        else:
            self.tail = None
            return None