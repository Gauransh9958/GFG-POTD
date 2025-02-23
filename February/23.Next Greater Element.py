
from collections import deque


class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        s = deque()
        res = [0] * n
        for i in range(n - 1, -1, -1):
            while len(s) and s[-1] <= arr[i]:
                s.pop()

            res[i] = -1 if not len(s) else s[-1]

            s.append(arr[i])

        return res