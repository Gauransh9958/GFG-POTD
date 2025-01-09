

class Solution:
    def subarraySum(self, arr, target):
        s = 0
        curr = 0

        for e in range(len(arr)):
            curr += arr[e]

            while curr > target and s < e:
                curr -= arr[s]
                s += 1

            if curr == target:
                return [s + 1, e + 1]

        return [-1]