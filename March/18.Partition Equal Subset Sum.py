class Solution:

    def equalPartition(self, arr):

        arrSum = sum(arr)


        if arrSum % 2 != 0:
            return False

        arrSum = arrSum // 2

        n = len(arr)
        prev = [False] * (arrSum + 1)
        curr = [False] * (arrSum + 1)

        prev[0] = True

        for i in range(1, n + 1):
            for j in range(arrSum + 1):
                if j < arr[i - 1]:
                    curr[j] = prev[j]
                else:
                    curr[j] = (prev[j] or prev[j - arr[i - 1]])

            prev = curr.copy()

        return prev[arrSum]