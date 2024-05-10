# Define a class Node to represent each element of the linked list
class Node:
    # Constructor to initialize each Node with a data value and a reference to the next Node
    def __init__(self, data):
        self.data = data  # Store the data value
        self.next = None  # Initialize the reference to the next Node as None

# Define a class LinkedList to represent the linked list itself
class LinkedList:
    # Constructor to initialize the linked list with a head Node
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    # Method to add a new Node with a given data value to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new Node with the given data
        if self.head is None:  # Check if the linked list is empty
            self.head = new_node  # If it is, set the new Node as the head
            return
        last_node = self.head  # Initialize a pointer to traverse the linked list
        while last_node.next:  # Traverse the linked list until the last Node is reached
            last_node = last_node.next
        last_node.next = new_node  # Set the next reference of the last Node to the new Node

    # Method to display the elements of the linked list
    def display(self):
        current_node = self.head  # Initialize a pointer to traverse the linked list starting from the head
        while current_node:  # Iterate until the end of the linked list
            print(current_node.data, end=" ")  # Print the data of the current Node
            current_node = current_node.next  # Move to the next Node
        print()  # Print a newline after displaying all elements

# Create a LinkedList object
linked_list = LinkedList()

# Append some elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Display the elements of the linked list
linked_list.display()
