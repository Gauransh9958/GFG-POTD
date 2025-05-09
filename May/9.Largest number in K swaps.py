

class Solution:

    def match(self, curr, res):

        if curr > res:
            res = curr
        return res

    def setDigit(self, s, index, res, k):

        if k == 0 or index == len(s) - 1:
            res = self.match(s, res)
            return res

        maxDigit = 0

        for i in range(index, len(s)):
            maxDigit = max(maxDigit, int(s[i]))

        if int(s[index]) == maxDigit:
            res = self.setDigit(s, index + 1, res, k)
            return res

        for i in range(index + 1, len(s)):

            if int(s[i]) == maxDigit:

                s = self.swap(s, index, i)

                res = self.setDigit(s, index + 1, res, k - 1)

                s = self.swap(s, index, i)

        return res

    def swap(self, s, i, j):

        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        return ''.join(s_list)

    def findMaximumNum(self, s, k):
        res = s
        res = self.setDigit(s, 0, res, k)

        return res

