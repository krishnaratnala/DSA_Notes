class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertion_at_begin(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # Update tail if the list was empty
            self.tail = new_node
        self.size += 1

    def insertion_at_end(self, val):
        new_node = Node(val)
        if self.head is None:  # If the list is empty, use insertion_at_begin
            self.insertion_at_begin(val)
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, val):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insertion_at_begin(val)
            return
        if index == self.size:
            self.insertion_at_end(val)
            return
        new_node = Node(val)
        temp = self.head
        for i in range(1, index):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("Deleting from an empty list")
        val = self.head.val
        self.head = self.head.next
        if self.head is None:  # If the list becomes empty, update the tail
            self.tail = None
        self.size -= 1
        return val

    def delete_last(self):
        if self.head is None:
            raise IndexError("Deleting from an empty list")
        if self.size == 1:  # If there's only one element
            val = self.head.val
            self.head = None
            self.tail = None
            self.size -= 1
            return val
        temp = self.head
        for i in range(self.size - 2):  # Find the second-to-last element
            temp = temp.next
        val = self.tail.val
        self.tail = temp
        self.tail.next = None
        self.size -= 1
        return val

    def printll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

# Create a LinkedList instance
s1 = LinkedList()

# Insert elements at the beginning
s1.insertion_at_begin(3)
s1.insertion_at_begin(2)
s1.insertion_at_begin(1)
s1.insertion_at_begin(8)

# Insert elements at the end
s1.insertion_at_end(4)
s1.insertion_at_end(5)
s1.insertion_at_end(9)

# Insert an element at a specific index
s1.insert(2, 10)  # Insert 10 at index 2

# Delete the first element
print("Deleted first element:", s1.delete_first())

# Delete the last element
print("Deleted last element:", s1.delete_last())

# Print the size of the linked list
print("Size of the linked list:", s1.size)

# Print the linked list
s1.printll()
list