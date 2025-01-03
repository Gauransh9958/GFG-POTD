class Solution:

    def subarrayXor(self, arr, m):
        res = 0

        mp = {}

        prefXOR = 0

        for val in arr:
            prefXOR ^= val

            res += mp.get(prefXOR ^ k, 0)

            if prefXOR == k:
                res += 1

            mp[prefXOR] = mp.get(prefXOR, 0) + 1

        return res