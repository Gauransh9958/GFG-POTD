class Solution:
    @staticmethod
    def subArraySum(arr, tar):
        sum_count = {}
        cumulative_sum = 0
        count = 0

        sum_count[0] = 1

        for num in arr:
            cumulative_sum += num

            if (cumulative_sum - tar) in sum_count:
                count += sum_count[cumulative_sum - tar]

            sum_count[cumulative_sum] = sum_count.get(cumulative_sum, 0) + 1

        return count