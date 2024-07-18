class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_end(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, val, index):
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return
        if index == 0:
            self.insert_first(val)
            return
        if index == self.size:
            self.insert_end(val)
            return
        new_node = Node(val)
        temp = self.head
        for i in range(1, index):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        self.size += 1

    def printll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

s1 = double_linked_list()
s1.insert_first(3)
s1.insert_first(4)
s1.insert_end(6)
s1.insert(1, 2)  # Insert 1 at index 2
s1.printll()
