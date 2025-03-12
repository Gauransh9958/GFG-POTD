

class Solution:
    def minCostClimbingStairs(self, cost):
        N = len(cost)
        climb_one = climb_two = 0

        for i in range(2, N + 1):

            res = climb_one

            climb_one = min(climb_one + cost[i - 1], climb_two + cost[i - 2])

            climb_two = res

        return climb_one