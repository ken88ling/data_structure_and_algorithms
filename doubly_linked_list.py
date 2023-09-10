class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Pushes a new node to the front of the list."""
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        """Appends a new node to the end of the list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def delete(self, data):
        """Deletes a node with the given data."""
        current = self.head

        # If head node itself holds the key to be deleted
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        while current:
            if current.data == data:
                break
            current = current.next

        # If key was not present in linked list
        if current is None:
            return

        # Update next and previous node pointers
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def display(self):
        """Displays the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" <-> ".join(map(str, nodes)))


# Test the DLL
dll = DoublyLinkedList()
dll.push(3)
dll.push(2)
dll.push(1)
dll.append(4)
dll.display()  # Outputs: 1 <-> 2 <-> 3 <-> 4

dll.delete(2)
dll.display()  # Outputs: 1 <-> 3 <-> 4
