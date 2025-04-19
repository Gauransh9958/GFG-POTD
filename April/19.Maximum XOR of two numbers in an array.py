class Node:

    def __init__(self):
        self.one = None
        self.zero = None


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, n):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            if bit == 0:
                if not curr.zero:
                    curr.zero = Node()
                curr = curr.zero

            else:
                if not curr.one:
                    curr.one = Node()
                curr = curr.one

    def findXOR(self, n):
        curr = self.root
        res = 0

        for i in range(31, -1, -1):
            bit = (n >> i) & 1

            if bit == 0:

                if curr.one:
                    curr = curr.one
                    res += (1 << i)
                else:
                    curr = curr.zero

            else:

                if curr.zero:
                    curr = curr.zero
                    res += (1 << i)
                else:
                    curr = curr.one
        return res


class Solution:

    def maxXor(self, arr):
        res = 0
        t = Trie()

        t.insert(arr[0])

        for i in range(1, len(arr)):
            res = max(t.findXOR(arr[i]), res)
            t.insert(arr[i])
        return res
