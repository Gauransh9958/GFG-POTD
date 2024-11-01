
class Solution:
    def maxSum(self, arr):
        arr.sort()
        
        n = len(arr)
        arranged = []
        i, j = 0, n - 1
        
        while i <= j:
            if i != j:
                arranged.append(arr[i])
                arranged.append(arr[j])
            else:
                arranged.append(arr[i])
            i += 1
            j -= 1

        max_sum = 0
        for k in range(n):
            max_sum += abs(arranged[k] - arranged[(k + 1) % n])
        
        return max_sum