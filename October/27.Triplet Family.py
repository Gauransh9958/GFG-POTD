class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        element_set = set(arr)

        for i in range(n):
            for j in range(i + 1, n):
                target = arr[i] + arr[j]
                if target in element_set:
                    return True
        
        return False