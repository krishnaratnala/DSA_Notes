class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class circular_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_first(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.size += 1


    def insert_at_end(self,val):
        new_node=Node(val)
        if self.tail is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1
    def insert(self,val,index):
        new_node=Node(val)
        temp=self.head
        if index==0:
            self.insert_at_first(new_node)
            return
        if index==self.size:
            self.insert_at_end(new_node)
            return
        for i in  range(index-1):
            temp=temp.next
        new_node.prev=temp
        new_node.next=temp.next
        temp.next=new_node

        self.size+=1
    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        for _ in range(self.size):
            print(temp.val, end=" -> ")
            temp = temp.next
        print("Head")
s1 = circular_linked_list()
s1.insert_at_first(3)
s1.insert_at_first(4)
s1.insert_at_first(7)
s1.insert_at_end(8)
s1.insert_at_end(9)
s1.insert(6,1)
s1.insert(5,3)
s1.printll()
