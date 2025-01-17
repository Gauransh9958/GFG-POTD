class Solution:

    def productExceptSelf(self, arr):
        n = len(arr)

        product = 1
        zeroCount = 0

        for num in arr:
            if num == 0:
                zeroCount += 1
            else:
                product *= num

        if zeroCount > 1:
            return [0] * n

        if zeroCount == 1:
            return [product if num == 0 else 0 for num in arr]

        return [product // num for num in arr]