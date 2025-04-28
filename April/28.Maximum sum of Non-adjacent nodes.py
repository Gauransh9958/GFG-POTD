

class Solution:
    def maxSumHelper(self, root):

        if (root == None):
            sum = [0, 0]
            return sum

        sum1 = self.maxSumHelper(root.left)
        sum2 = self.maxSumHelper(root.right)
        sum = [0, 0]

        sum[0] = sum1[1] + sum2[1] + root.data

        sum[1] = (max(sum1[0], sum1[1]) + max(sum2[0], sum2[1]))
        return sum

    def getMaxSum(self, root):

        res = self.maxSumHelper(root)
        return max(res[0], res[1])

