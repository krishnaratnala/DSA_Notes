class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class linked_list_rec:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
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
    def insert(self,index,val):
        new_node=Node(val)

        def dfs(current_index,temp):
            if index == 0:  # Special case: insertion at the beginning
                self.insertion_at_begin(val)
            elif self.head is None and index > 0:  # Special case: insert in an empty list at non-zero index
                raise IndexError("Index out of bounds")
            if current_index==index-1:
                new_node.next = temp.next
                temp.next = new_node
                self.size+=1
                if new_node.next is None:  # Update tail if inserted at the end
                    self.tail = new_node
                return True
            elif temp is None or current_index>=self.size:
                return  False
            else:
               return dfs(current_index+1,temp.next)
        dfs(0,self.head)

    def printll(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
s1=linked_list_rec()
s1.insertion_at_begin(1)
s1.insertion_at_begin(2)
s1.insertion_at_begin(3)
s1.insertion_at_begin(4)
s1.insert(2,6)
s1.printll()