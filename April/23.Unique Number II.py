class Solution:

    def singleNum(self, arr):

        xor_val = 0
        for i in arr:
            xor_val ^= i

        xor_val &= -xor_val

        res = [0, 0]

        for num in arr:

            if (num & xor_val) == 0:
                res[0] ^= num

            else:
                res[1] ^= num

        if res[0] > res[1]:
            res[0], res[1] = res[1], res[0]

        return res

