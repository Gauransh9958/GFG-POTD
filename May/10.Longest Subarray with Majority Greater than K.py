def longestSubarray(arr, k):
    n = len(arr)
    trans = [1 if num > k else -1 for num in arr]
    
    first_occurrence = {}
    max_length = 0
    prefix_sum = 0

    for i in range(n):
        prefix_sum += trans[i]

        if prefix_sum > 0:
            max_length = i + 1
        else:
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
            if (prefix_sum - 1) in first_occurrence:
                max_length = max(max_length, i - first_occurrence[prefix_sum - 1])

    return max_length
