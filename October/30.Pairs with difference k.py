from collections import defaultdict

class Solution:
    def countPairsWithDiffK(self, arr, k):
        freq = defaultdict(int)
        count = 0

        for num in arr:
            freq[num] += 1

        for num in freq:
            if k > 0 and (num + k) in freq:
                count += freq[num] * freq[num + k]
            elif k == 0 and freq[num] > 1:
                count += freq[num] * (freq[num] - 1) // 2

        return count
