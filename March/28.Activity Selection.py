class Solution:

    def activitySelection(self, start, finish):
        ans = 0

        arr = []

        for i in range(len(start)):
            arr.append((finish[i], start[i]))

        arr.sort()

        finishtime = -1

        for i in range(len(arr)):
            activity = arr[i]
            if activity[1] > finishtime:
                finishtime = activity[0]
                ans += 1

        return ans

