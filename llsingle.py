# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the value
        self.next = None  # Pointer to the next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    # ✅ Search for a value
    def search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.data == target:
                return index  # Found at this position
            temp = temp.next
            index += 1
        return -1  # Not found