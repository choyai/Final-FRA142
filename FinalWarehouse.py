import requests, json
import urllib.parse
import random
import msvcrt #for input w/o enter
import getpass #hidden password
import hashlib #sha 256
from Node import Node
from Queue import Queue
from LinkedList import LinkedList
from hashTable import hashTable
from QuickSort import quickSort
import os
### login >>> logged

account = {'aob' : 'e98aa696f879014ecd59d36f7feaa5f35c05cded570f2e469e63c4ab8f3a79ce:2dd8fa84f6544d039b0e8657d311bf0b',
           'chaiyo': '38dc0382cc68f3922d2be5241182ec53128667a8eeaf44cc84df81744f644dff:3e9668b89af7432aba62087f82dda83d',
           'aj.blink' : 'bab5f01ce09d7c31b9d4ca7d801535b962e6ff7428bdcbcb13b590ac708a6286:465ec34d649a4aed8f7e5ce3c46a346d'} #pass for aj.blink is lnwdota
class _Getch:
    #Gets a single character from standard input.  Does not echo to the screen.
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchWindows: #getch for windows
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def lineotp(): #One Time Password sent through Line notify-api
 LINE_ACCESS_TOKEN = "cq8ud1LVKkveYopDkfQH0l9P1JKZugC5lBaU4pzdtvA"
 url = "https://notify-api.line.me/api/notify"
 password = ""
 for i in range(6):  # random otp
  password = password + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@') # random password
 message = "OTP : " + password  # pack msg
 msg = urllib.parse.urlencode({"message": message})
 LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN}
 session = requests.Session()
 a = session.post(url, headers=LINE_HEADERS, data=msg)
 print("OTP has been sent. Please check your line")
 #print(a.text) #status msg
 return(password)

def linemsg(message): #Other messages sent through Line notify-api
 LINE_ACCESS_TOKEN = "cq8ud1LVKkveYopDkfQH0l9P1JKZugC5lBaU4pzdtvA" #manually generated(through line's website) access token.
 url = "https://notify-api.line.me/api/notify"
 msg = urllib.parse.urlencode({"message": message})
 LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN}
 session = requests.Session()
 a = session.post(url, headers=LINE_HEADERS, data=msg)
 # print(a.text) #status msg

def login():#login function
  x=0
  UserName = input("Enter Username: ") #username input
  if UserName in account: #check username
      hashed_password = account[UserName] #get hashed password from database
      pswd = getpass.getpass('Password:') #password input without showing
      pswd = str(pswd)
      password, salt = hashed_password.split(':') #split password and salt
      pswd = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest() #cryption password that user input
      if (str(pswd)==password): #check hashed password
        passwordotp = lineotp() # send otp to line
        while (x<4): # conditon to limit otp input
                PassWord = input ("Enter Password: ") #input otp
                if str(PassWord) == passwordotp: #check otp
                    print ("Login successful!")
                    linemsg(UserName + " has been logged in")
                    logged(UserName)#run main loop
                    break
                else:
                    print ("Password did not match!. Please try again.")
                    x+=1
      else:
            print("Wrong password input")
  else:
      print("User not found!.")

def logged(x):#Main program
    UserName = x
    #define functions
    def executeCommand(Command): #Command execute function
        Command = Command.lower()
        if len(Command) < 5:  #avoid index range errors
            Command = " "
        if Command[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # Check for each command
            if Command[0] == '0': #Retrieve Product
                ID = Command[1:5]
                whKey = Command[1]
                RowKey = Command[2]
                Slot = Command[3:5]
                x = FindX(Slot)
                y = FindY(Slot)
                hashedkey = warehouseDict.hash(whKey)
                warehouse = warehouseDict.table[hashedkey].item
                row = warehouse[int(RowKey) - 1]
                if CheckAvai(row, x, y) == False:
                    if CheckBeltAvai() == True:
                        belt.add(Node(row[x][y]))
                        row[x][y] = None
                        print("Getting product ID: " + ID.upper() + " from Warehouse" + warehouseDict.table[
                            hashedkey].name.upper() + " Row" + RowKey + " from slot number " + Slot)
                        print("Placing product ID: " + ID.upper() + " on the belt")
                        print("\n -------------------------------------------------------------------- \n")
                        return True
                    else:
                        print("Conveyor belt is full. Cannot place the product")
                        print("\n -------------------------------------------------------------------- \n")
                        return False
                else:
                    print("Slot is empty; cannot retrieve product")
                    print("\n -------------------------------------------------------------------- \n")
                    return False

            elif Command[0] == '1': #Insert product
                ID = Command[1:5]
                whKey = Command[1]
                RowKey = Command[2]
                Slot = Command[3:5]
                hashedkey = warehouseDict.hash(whKey)
                warehouse = warehouseDict.table[hashedkey].item
                row = warehouse[int(RowKey) - 1]
                x = FindX(Slot)
                y = FindY(Slot)
                if CheckAvai(row, x, y) == True:
                    row[x][y] = ID
                    print("Storing product: " + ID.upper() + " from Warehouse" + warehouseDict.table[
                        hashedkey].name.upper() + " Row" + RowKey + " from slot number " + Slot)
                    print("Stored successfully")
                    print("\n -------------------------------------------------------------------- \n")
                    return True
                else:
                    print("Slot is occupied; cannot store the product.")
                    print("\n -------------------------------------------------------------------- \n")
                    return False

            elif Command[0] == '2': #Sort row.
                ID = Command[1:5]
                whKey = Command[1]
                RowKey = (Command[2])
                hashedkey = warehouseDict.hash(whKey)
                warehouse = warehouseDict.table[hashedkey].item
                row = warehouse[int(RowKey) - 1]
                #print(row)
                row = rowSort(row)
                #print(row)
                print(
                    "Warehouse" + warehouseDict.table[hashedkey].name.upper() + " Row " + RowKey + " has been sorted.")
                print("\n -------------------------------------------------------------------- \n")
                return True

            elif Command[0] == '3': #Belt retrieval
                if belt.size != 0:
                    print("Retrieving product with ID: " + belt.remove() + " from the belt.")
                    print("There are now " + str(belt.size) + " products on the belt.")
                    print("\n -------------------------------------------------------------------- \n")
                    return True
                else:
                    print("No products to retrieve!")
                    print("\n -------------------------------------------------------------------- \n")
                    return False

            elif Command[0] == '4': #prints the content of each warehouse in order by row
                for whKey in warehouseDict.table:
                    warehouse = whKey.item
                    count = 0
                    print("Warehouse" + whKey.name.upper())
                    print("Number of Rows: 5") #phase1: item count.
                    for row in warehouse:
                        for x in range(len(row)):
                            for y in range(len(row)):
                                if row[x][y] != None:
                                    count += 1
                    print("Total products: " + str(count))
                    for row in range(len(warehouse)): #phase2: Display each row
                        txt = "Products in Row" + str(row + 1) + ":"
                        for x in range(len(warehouse[row])):
                            for y in range(len(warehouse[row])):
                                if warehouse[row][x][y] != None:
                                    txt += " " + warehouse[row][x][y].upper() + " "
                                    count += 1
                        txt += "\n"
                        print(txt)
                print("\n -------------------------------------------------------------------- \n")
                return True

            elif Command[0] == '5': #Search
                result = idiotSearch(Command)
                if result != None:
                    print("\n -------------------------------------------------------------------- \n")
                    return True
                print("\n -------------------------------------------------------------------- \n")
                return False

            elif Command[0] == '9':
                if len(Command) < 9:
                    Command = ''
                    pass
                searchkey = Command[0:5]
                searchResult = idiotSearch(searchkey)
                ID = Command[1:5]
                NewID = Command[6:10]
                NewKey = Command[5]
                NewRowKey = Command[6]
                NewSlot = Command[7:9]
                newx = FindX(NewSlot)
                newy = FindY(NewSlot)
                newhash = warehouseDict.hash(NewKey)
                newWarehouse = warehouseDict.table[newhash].item
                newrow = newWarehouse[int(NewRowKey) - 1]

                if searchResult != None: #phase1, was the item found?
                    if CheckAvai(newrow, newx, newy) == False:
                        print("Slot is occupied. Failed to move.")
                        print("\n -------------------------------------------------------------------- \n")
                        return False
                    else:
                        whKey = searchResult[0]
                        RowKey = searchResult[1]
                        Slot = searchResult[2:4]
                        hashedkey = warehouseDict.hash(whKey)
                        warehouse = warehouseDict.table[hashedkey].item
                        row = warehouse[int(RowKey) - 1]
                        x = FindX(Slot)
                        y = FindY(Slot)
                        newrow[newx][newy] = row[x][y]
                        row[x][y] = None
                        print("Moved product " + ID.upper() + " to " + NewID.upper())
                        print("\n -------------------------------------------------------------------- \n")
                        return True
                else:
                    print("\n -------------------------------------------------------------------- \n")
                    return False
        else:
            print("Incorrect command syntax")
            print("\n -------------------------------------------------------------------- \n")
            return  False


    def FindX(Slot):
        if len(Slot) == 2:
            x = int(Slot[0])
            return x
        else:
            print("Unknown slot input")

    def FindY(Slot):
        if len(Slot) == 2:
            y = int(Slot[1])
            return y
        else:
            print("Unknown slot input")

    def CheckAvai(row, x, y):
        if row[x][y] == None:
            return True
        else:
            return False

    def linemsg(message):
        LINE_ACCESS_TOKEN = "cq8ud1LVKkveYopDkfQH0l9P1JKZugC5lBaU4pzdtvA"
        url = "https://notify-api.line.me/api/notify"
        msg = urllib.parse.urlencode({"message": message})
        LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded',
                        "Authorization": "Bearer " + LINE_ACCESS_TOKEN}
        session = requests.Session()
        a = session.post(url, headers=LINE_HEADERS, data=msg)
        # print(a.text) #status msg

    def CheckBeltAvai():
        return belt.size < 10

    def rowSort(row):
        row1D = []
        for x in range(len(row)):
            for y in range(len(row)):
                if row[x][y] != None:
                    row1D.append(row[x][y])
                    #print(row[x][y])
        #print(row1D)
        quickSort(row1D)
       # print(row1D)
        for x in range(len(row)):
            for y in range(len(row)):
                row[x][y] = None
        #print(row)
        for i in range(len(row1D)):
            #print(i)
            x = 0
            for y in range(len(row)):
                if len(row) * x + y == len(row1D):
                    return True
                else:
                    row[x][y] = row1D[len(row) * x + y]

    def idiotSearch(Command):
        ID = Command[1:5]
        whKey = Command[1]
        RowKey = Command[2]
        Slot = Command[3:5]
        hashedkey = warehouseDict.hash(whKey)
        warehouse = warehouseDict.table[hashedkey].item
        row = warehouse[int(RowKey) - 1]
        x = FindX(Slot)
        y = FindY(Slot)
        if row[x][y] == ID:
            print("Found the product at " + ID.upper())
            return ID
        else:
            for whKey in warehouseDict.table:
                warehouse = whKey.item
                for row in range(len(warehouse)):
                    for x in range(len(warehouse[row])):
                        for y in range(len(warehouse[row])):
                            if warehouse[row][x][y] == ID:
                                print("Found the product at " + whKey.name.upper() + str(row + 1) + str(x) + str(
                                    y))
                                return whKey.name + str(row + 1) + str(x) + str(y)
            print("Product not found")
            return None
    # Initialize
    warehouseDict = hashTable(5)
    warehouseA = []
    warehouseB = []
    warehouseC = []
    warehouseD = []
    warehouseE = []
    warehouseDict.add("a", warehouseA)
    warehouseDict.add("b", warehouseB)
    warehouseDict.add("c", warehouseC)
    warehouseDict.add("d", warehouseD)
    warehouseDict.add("e", warehouseE)
    #warehouseDict.printtable()
    for warehouse in warehouseDict.table:
        for i in range(1, 4):
            warehouse.item.append([[None for x in range(10)] for y in range(10)])
        for i in range(3, 5):
            warehouse.item.append([[None for x in range(8)] for y in range(8)])

    # warehouseDict = {'a': warehouseA, 'b': warehouseB, 'c': warehouseC, 'd': warehouseD, 'e': warehouseE}
    print("Warehouses generated")
    belt = Queue()
    print("Conveyor Belt Generated")
    commandQue = Queue()
    print("Input your commands")
    work = True
    while (work == True):
        print(" 0XXXX \n"
              "Retrieve a product with ID XXXX \n"
              "1XXXX \n"
              "Store a product with ID XXXX \n"
              "2XY00 \n"
              "Sort warehouse X at row Y \n"
              "30000 \n"
              "Retrieve a product from the conveyor belt \n"
              "40000 \n"
              "Output information on all of the warehouses \n"
              "5XXXX \n"
              "Search for a product ID XXXX \n"
              "9XXXXYYYY \n"
              "Manually put a product ID XXXX at position YYYY \n")
        newcom = True
        while newcom:
            comm = input("Please enter command\n")
            commandQue.add(Node(comm))
            yesno = ''
            while yesno != b'y' and yesno != b'n' and yesno != b'Y' and yesno != b'N':
                print("Would you like to enter another command? y/n\n")
                yesno = msvcrt.getch() #get pressing key
            if yesno == b'n' or yesno == b'N':
                newcom = False
        # Execution
        strmsg = "command log" #create a command log
        c=0
        for i in range(commandQue.size):
            c+=1
            tempp = commandQue.remove().upper()
            bool = executeCommand(tempp) #execute the command from the command Queue
            if bool == True : #if command is executed succussfully, add to the log
                if c == 1:
                    strmsg += ": " + tempp
                else:
                    strmsg += ", " + tempp

        linemsg(strmsg)

        out = ' ' #logout prompt
        while (out != b'y' and out != b'n' and out != b'Y' and out != b'N') :
            print("Would you like to logout? y/n\n")
            out= msvcrt.getch()#get pressing key
        if out == b'y' or out == b'Y':
            print("See you again!")
            linemsg(UserName + " has been loged out")
            work = False
            break #return to login


while True:
    print ("Welcome to the warehouse")
    login()  #loop login
