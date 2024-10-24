class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)

        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0

        result = []
        zero_count = 0

        for num in arr:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1

        result.extend([0] * zero_count)

        for i in range(n):
            arr[i] = result[i]

        return arr
