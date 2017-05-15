from Node import Node
class hashTable:
#Part 1
    def __init__(self, size = 100, table = []):#Initialize with default size at 100
        self.size = size
        self.table = table
        for i in range(self.size):
            self.table.append(Node())
    def hash(self, key):
        keyhash = 0
        for i in range(len(key)):
            a = key[i]
            b = ord(a)
            keyhash = (keyhash + b)
        keyhash = keyhash + 3
        index = keyhash % self.size
        #print(index)
        return index
    def add(self, key, item):
        index = self.hash(key) #hash the key
        bucket = self.table[index]
        #print(bucket.name)
        if bucket.name == None: #insert if the bucket(index) is empty
            bucket.name = key
            bucket.item = item
        else: #insert into a linked list of bucket is not empty
            while bucket.next != None:
                temp = bucket
                bucket = bucket.next
                bucket.previous = temp
            bucket.next = Node(key, item)
            bucket.next.previous = bucket
    def delete(self, key): #like search but also deletes Node
        index = self.hash(key)
        current = self.table[index]
        if current.name == key:
            current.name = None
            current.item =None
            print("deleted")
            return True
        else:
            while current.next != None:
                if current.name == key:
                    current.delete()
                    print("Deleted")
                    return True
                else:
                    current = current.next
            if current.name == key:
                current.delete()
                print("Deleted")
                return True
            else:
                print("Not found")
                return False
    def printtable(self): #prints entire hash table
        for i in range(self.size - 1):
            self.printindex(i)
    def printindex(self, index): #prints each index of the table
        current = self.table[index]
        print("Index: " + str(index))
        while current.next != None:
            print("Key: " + str(current.name))
            print("Value: " + str(current.item))
            current = current.next
        print("Key: " + str(current.name))
        print("Value: " + str(current.item))
    def search(self, key):
        index = self.hash(key)
        current = self.table[index]
        if current.name == key:
            return current.item
        else:
            while current.next != None: #Avoids NoneType object errors while iterating
                if current.name == key:
                    return current.item
                else:
                    current = current.next #iterate through linked list
            if current.name == key:
                return current.item
            else:
                return "Not found"
