class Node:
    def __init__(self, name: object = None,item = None, next: object = None, previous: object = None, upper: object = None) -> object:
        self.name = name
        self.item = item
        self.previous = previous
        self.upper = upper
        self.next = next
    def __str__(self):
        return str(self.name)
    def delete(self):
        self.name = None
        self.previous.next = self.next
