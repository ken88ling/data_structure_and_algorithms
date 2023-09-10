import random


class Node:
    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [None] * height


class SkipList:
    def __init__(self):
        self.head = Node()
        self.len = 0
        self.maxHeight = 0

    def _iterNodes(self, elem):
        # Helper to iterate over the nodes that should be updated on an insert.
        current = self.head
        for level in range(self.maxHeight - 1, -1, -1):
            while True:
                future = current.next[level]
                if future is None or future.elem >= elem:
                    break
                current = future
            yield current, level

    def find(self, elem, update=None):
        # Find and return the node with the given element.
        if update is None:
            update = self.updateList(elem)
        if len(update) > 0:
            nextNode = update[0].next[0]
            if nextNode is not None and nextNode.elem == elem:
                return nextNode
        return None

    def contains(self, elem, update=None):
        return self.find(elem, update) is not None

    def randomHeight(self):
        # Randomly decide the height of a new node.
        height = 1
        while random.random() < 0.5 and height < 32:  # Limit max height to 32.
            height += 1
        return height

    def updateList(self, elem):
        # Return the list of nodes that need to be updated at each level.
        update = [None] * self.maxHeight
        for prev, level in self._iterNodes(elem):
            update[level] = prev
        return update

    def insert(self, elem):
        node = Node(self.randomHeight(), elem)
        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)
        update = self.updateList(elem)
        if self.find(elem, update) is None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def remove(self, elem):
        update = self.updateList(elem)
        node = self.find(elem, update)
        if node:
            for i in range(len(node.next)):
                update[i].next[i] = node.next[i]
                if self.head.next[i] is None:
                    self.maxHeight -= 1
            self.len -= 1


# Test SkipList
s = SkipList()
s.insert(3)
s.insert(2)
s.insert(1)
print(s.contains(3))  # True
s.remove(2)
print(s.contains(2))  # False
