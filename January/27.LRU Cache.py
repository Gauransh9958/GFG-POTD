

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.pre = None


class LRUCache:
    hsmap = dict()
    capacity = count = 0
    head = tail = None

    def __init__(self, cap):
        self.hsmap = dict()
        self.capacity = cap
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.head.pre = None
        self.tail.next = None
        self.tail.pre = self.head
        count = 0

    def addToHead(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def get(self, key):

        if key in self.hsmap:

            node = self.hsmap[key]
            result = node.value
            self.deleteNode(node)
            self.addToHead(node)

            return result

        else:
            return -1

    def put(self, key, value):

        if key in self.hsmap:

            node = self.hsmap[key]
            node.value = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node = Node(key, value)
            self.hsmap[key] = node

            if self.count < self.capacity:
                self.count += 1
                self.addToHead(node)
            else:
                self.hsmap.pop(self.tail.pre.key)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)