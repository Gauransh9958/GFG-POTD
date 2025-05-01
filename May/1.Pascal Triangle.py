class Solution:

    def nthRowOfPascalTriangle(self, n):
        n -= 1

        res = []

        prev = 1
        res.append(prev)

        for i in range(1, n + 1):

            curr = (prev * (n - i + 1)) // i
            res.append(curr)
            prev = curr

        return res

