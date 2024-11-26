
def circularSubarraySum(arr):
    def kadane(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
    max_kadane = kadane(arr)
    
    total_sum = sum(arr)
    
    def min_kadane(arr):
        min_sum = float('inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            min_sum = min(min_sum, current_sum)
            if current_sum > 0:
                current_sum = 0
        return min_sum
    
    min_kadane_sum = min_kadane(arr)
    
    if total_sum == min_kadane_sum:
        return max_kadane
    
    max_circular_sum = total_sum - min_kadane_sum
    
    return max(max_kadane, max_circular_sum)
