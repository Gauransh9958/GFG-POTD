class Solution:

    def countWays(self, n):
        if n <= 1:
            return 1

        a, b = 1, 1

        for i in range(2, n + 1):
            temp = a + b

            a = b
            b = temp

        return b
