class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]
        def canPlaceCows(stalls, k, dist):
            count = 1
            last_position = stalls[0]

            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= dist:
                    count += 1
                    last_position = stalls[i]
                if count == k:
                    return True
            return False

        best_distance = 0
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(stalls, k, mid):
                best_distance = mid
                low = mid + 1
            else:
                high = mid - 1

        return best_distance
