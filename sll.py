# SinglyLinkedList
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.dummy = Node("Dummy Node")  # This is the dummy node
        self.head = self.dummy

    def push(self, data):
        """Pushes a new node to the front of the list."""
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def pop(self):
        """Pops the front node of the list."""
        if not self.head.next:
            print("List is empty!")
            return None
        popped_data = self.head.next.data
        self.head.next = self.head.next.next
        return popped_data

    def add_after_value(self, target_data, new_data):
        """Adds a node after a specific value."""
        current = self.head
        while current.next:
            if current.next.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next.next
                current.next.next = new_node
                return
            current = current.next

    def display(self):
        """Displays the list."""
        nodes = []
        current = self.head.next  # We start from the node after dummy node
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
