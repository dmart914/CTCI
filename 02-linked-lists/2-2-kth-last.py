# 2-2 Implement an algorithm to find the kth to last element of a
# a singly linked list

# Pseudo:
# Iterate through all to find the length
# Iterate again to get the kth last

class Node:
    '''A node in a singly linked list'''

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return (str(self.data))

class LinkedList:
    '''A linked list comprised of Nodes'''

    def __init__(self, start=None):
        self.start = start
        self.current = start
        self.last = start

    def __str__(self):
        returnString = 'LINKED LIST\n'
        returnString += 'Current node data: '
        returnString += str(self.current)
        return returnString

    def next(self):
        if self.current == None:
            return False
        elif self.current.next == None:
            return False
        else:
            self.current = self.current.next
            return self.current

    def reset(self):
        self.current = self.start

    # Pushes to the END; sets the current pointer to the
    # node pushed, or the last nonde
    def push(self, n):
        if self.start == None:
            print('start')
            self.start = n
            return

        if (self.current == None):
            print('resetting')
            self.reset()

        while (self.current.next != None):
            self.next()

        self.current.next = n
        self.next()

    def printAll(self):
        self.reset()
        print('LINKED LIST')
        currentNodeIndex = 1
        while self.next() != False:
            print(str(currentNodeIndex) + ' ' + str(self.current))
            currentNodeIndex += 1
            # self.next()

        self.reset()

    def findKLast(self, n):
        if (self.start == None):
            return False

        listLength = 0
        self.reset()

        for i in range(0, n):
            listLength += 1
            if (self.next() == False):
                return False

        nodeToReturn = self.start

        while(self.next() != False):
            listLength += 1
            nodeToReturn = nodeToReturn.next


        nodeIndexToReturn = listLength - int(n)
        return [nodeIndexToReturn, str(nodeToReturn)]

myLinkedList = LinkedList(Node('Dave'))
print(myLinkedList)
myLinkedList.next()
myLinkedList.next()
myLinkedList.next()
print(myLinkedList)
myLinkedList.reset()
print(myLinkedList)
myLinkedList.push(Node('Nora'))
myLinkedList.push(Node('Luca'))
myLinkedList.push(Node('Riley'))
myLinkedList.push(Node('lol'))
myLinkedList.push(Node('k'))
myLinkedList.printAll()

print(myLinkedList.findKLast(1))
