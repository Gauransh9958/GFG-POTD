


class Solution:
    def findUnion(self, a, b):
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
                
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1
        
        while i < len(a):
            if i == 0 or a[i] != a[i - 1]:
                result.append(a[i])
            i += 1

        while j < len(b):
            if j == 0 or b[j] != b[j - 1]:
                result.append(b[j])
            j += 1
            
        return result


