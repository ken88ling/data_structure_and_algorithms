class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Pushes a new node to the front of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Pops the front node of the list."""
        if not self.head:
            print("List is empty!")
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def add_after_value(self, target_data, new_data):
        """Adds a node after a specific value."""
        if not self.head:
            return
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def display(self):
        """Displays the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)))


# Test the SLL
sll = SinglyLinkedList()
sll.push(4)
sll.push(2)
sll.push(1)
sll.display()  # Outputs: 1 -> 2 -> 4

popped_value = sll.pop()
print(f"Popped Value: {popped_value}")  # Outputs: Popped Value: 1

sll.display()  # Outputs: 2 -> 4
