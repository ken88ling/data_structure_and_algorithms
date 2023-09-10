class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        p = Node(data)
        p.next = self.head
        self.head = p

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def add_after_value(self, target_data, new_data):
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
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)))


# Test the SLL
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(4)
sll.display()  # Outputs: 1 -> 2 -> 4

sll.add_after_value(2, 3)
sll.display()  # Outputs: 1 -> 2 -> 3 -> 4

sll.delete(2)
sll.display()
