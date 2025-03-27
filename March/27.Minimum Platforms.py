class Solution:

    def minimumPlatform(self, arr, dep):
        n = len(arr)
        order = []
        for i in range(n):
            order.append([arr[i], 'a'])
            order.append([dep[i], 'd'])

        order.sort(key=lambda x: x[1])
        order.sort()
        result = 1
        plat_needed = 0

        for i in order:
            if (i[1] == 'a'):
                plat_needed += 1
            else:
                plat_needed -= 1
            result = max(result, plat_needed)
        return result
