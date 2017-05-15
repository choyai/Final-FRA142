from LinkedList import LinkedList
from Node import Node
from StackClass import StackClass
from Queue import Queue
import datetime
import time
import random

def BubbleSort(list_linked):
    done = False
    while done == False:
        swap = False
        for i in range(list_linked.size - 1):
            item = list_linked.head
            for n in range(i):
                item = item.next
            if item.name > item.next.name:
                temp = item.name
                item.name = item.next.name
                item.next.name = temp
                swap = True
        if swap == False:
            done = True
            it = list_linked.head
            print(it)
            for i in range(list_linked.size):
                it = it.next
                print(it)

    return list_linked

qu = Queue()
for i in range(10):
    qu.add(Node(random.randint(1, 100)))
it = qu.head
print(it)
for i in range(qu.size - 1):
    it = it.next
    print(it)
BubbleSort(qu)