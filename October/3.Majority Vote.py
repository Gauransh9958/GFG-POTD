
class Solution:
    def findMajority(self, arr):
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in arr:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        threshold = len(arr) // 3
        result = []
        
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return sorted(result) if result else [-1]

