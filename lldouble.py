# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.prev = None  # Pointer to previous node
        self.next = None  # Pointer to next node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the front
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete a node with a given value
    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next

    # Display the list forward
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display the list backward
    def display_backward(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def reverse(self):
        temp = None
        current = self.head

        # Traverse the list and swap next and prev for each node
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev  # Move to the next node (which is prev now)

        # After loop, temp is at the previous node of the original head
        if temp:
            self.head = temp.prev  # New head of the list

