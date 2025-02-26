class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        
        pse = [-1] * n
        nse = [n] * n
        
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        
        result = [0] * (n + 1)
        
        for i in range(n):
            window_size = nse[i] - pse[i] - 1
            result[window_size] = max(result[window_size], arr[i])
        
        for i in range(n - 1, 0, -1):
            result[i] = max(result[i], result[i + 1])
        
        return result[1:]
