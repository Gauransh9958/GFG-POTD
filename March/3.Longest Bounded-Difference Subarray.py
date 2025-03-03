


def longestSubarray(arr, x):
    
    n = len(arr)
    
    beginning = 0
    maxLen = 1
    
    for i in range(n):
        for j in range(i, n):
            
            mini = float('inf')
            maxi = float('-inf')
            
            for k in range(i, j + 1):
                mini = min(mini, arr[k])
                maxi = max(maxi, arr[k])
            

            if maxi - mini <= x and maxLen < j - i + 1:
                maxLen = j - i + 1
                beginning = i
    
    return arr[beginning: beginning + maxLen]

if __name__ == "__main__":
    arr = [8, 4, 2, 6, 7]
    x = 4

    res = longestSubarray(arr, x)
    
    print(*res)