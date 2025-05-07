from typing import Optional
from collections import deque

from typing import List



class Solution:

    def printArray(self, ints):
        return list(ints)

    def printPathsUtil(self, node, path, paths):
        if node is None:
            return

        path.append(node.data)

        if node.left is None and node.right is None:
            paths.append(self.printArray(path))
        else:
            self.printPathsUtil(node.left, path, paths)
            self.printPathsUtil(node.right, path, paths)

        path.pop()

    def Paths(self, root):
        paths = []

        self.printPathsUtil(root, [], paths)

        return paths