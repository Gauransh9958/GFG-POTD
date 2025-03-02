from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        result = []
        deque_ = deque()

        for i in range(len(arr)):
            if deque_ and deque_[0] < i - k + 1:
                deque_.popleft()

            while deque_ and arr[deque_[-1]] < arr[i]:
                deque_.pop()
            deque_.append(i)

            if i >= k - 1:
                result.append(arr[deque_[0]])

        return result
