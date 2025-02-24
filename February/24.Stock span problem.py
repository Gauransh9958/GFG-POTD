
class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        s = []
        s.append(0)
        S = [0] * n

        S[0] = 1

        for i in range(1, n):

            while s and arr[s[-1]] <= arr[i]:
                s.pop()

            
            span = (i + 1) if not s else (i - s[-1])
            S[i] = span
            s.append(i)
        return S