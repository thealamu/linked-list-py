class Node:
    data = None
    next = None


class LinkedList:
    head = None
    sz = 0

    def size(self):
        return self.sz

    def empty(self):
        return self.head == None
