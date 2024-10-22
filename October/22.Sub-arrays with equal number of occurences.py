from collections import defaultdict

class Solution:
    def sameOccurrence(self, arr, x, y):
        count_x = count_y = 0
        prefix_diff = 0
        diff_count = defaultdict(int)
        diff_count[0] = 1
        result = 0

        for num in arr:
            if num == x:
                count_x += 1
            elif num == y:
                count_y += 1

            prefix_diff = count_x - count_y

            result += diff_count[prefix_diff]

            diff_count[prefix_diff] += 1

        return result