from collections import defaultdict


class Solution:

    # Function to find the length of the longest subarray with sum 'k'
    def longestSubarray(self, arr, k):
        # Creating a default dictionary
        # Default value for non-existent keys will be 0
        um = defaultdict(lambda: 0)

        # Initializing variables
        current_sum = 0
        maxLen = 0

        # Iterating through the array
        for i in range(len(arr)):  # Use len(arr) instead of n
            # Calculating the current sum
            current_sum += arr[i]

            if current_sum == k:
                maxLen = i + 1

            if current_sum not in um:
                um[current_sum] = i

            if (current_sum - k) in um:
            maxLen = max(maxLen, i - um[current_sum - k])

        # Returning the maximum subarray length
        return maxLen