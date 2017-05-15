from hashTable import hashTable
#stacki = StackClass()
#queue = Queue()
#print(str(queue.isEmpty))
#print(str(stacki.isEmpty))
#for i in range(10):
    #stacki.push(Node(i))
    #queue.add(Node(i))
    #print(Node(i))
#for i in range(10):
    #print(stacki.pop())
    #print(queue.remove())
#linked = LinkedList()
#for i in range(10):
#    linked.add(Node(i), i)
#for i in range(10):
#    print(linked.remove(i))

#house = hashTable()
#house.add("doh", "Don't")
#house.add("183834", "ddd")
#house.printtable()
#print(house.search("183834"))
#house.delete("doh")

house = hashTable(5)

al = "abcdefghijklmnopqrstuvwxy"
for i in al:
    print(house.hash(i))
house.hash("a")
