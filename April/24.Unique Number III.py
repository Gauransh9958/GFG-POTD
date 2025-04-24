
class Solution:

    def getSingle(self, arr):
        ones, twos = 0, 0

        for num in arr:

            twos |= ones & num

            ones ^= num

            mask = ~(ones & twos)
            ones &= mask
            twos &= mask

        return ones