from typing import List

class Solution:
    def findTriplets(self, arr: List[int]) -> List[List[int]]:
        res = []
        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        res.append([i, j, k])

        return res
