from collections import defaultdict


class Solution:

    def countDistinct(self, arr, k):
        mp = defaultdict(lambda: 0)
        n = len(arr)

        dist_count = 0
        for i in range(k):
            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

        res = []
        res.append(dist_count)

        for i in range(k, n):


            if mp[arr[i - k]] == 1:
                dist_count -= 1
            mp[arr[i - k]] -= 1


            if mp[arr[i]] == 0:
                dist_count += 1
            mp[arr[i]] += 1

            res.append(dist_count)

        return res