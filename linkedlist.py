class Node:
    data = None
    next = None


class LinkedList:
    head = Node()
    sz = 0

    def size(self):
        return self.sz

    def empty(self):
        return self.head == None

    def value_at(self, index):
        "Returns the value at index"
        if self.empty:
            raise IndexError("list is empty")
        node = self.head
        for _ in range(index):
            if node.next:
                node = node.next
            else:
                raise IndexError("index out of bounds")
        return node

    def push_front(self, value):
        value.next = self.head.next
        self.head.next = value
