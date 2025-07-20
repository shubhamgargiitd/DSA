# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end for testing
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 1. Delete from beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # 2. Delete from end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # 3. Delete at a specific position (0-based index)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
