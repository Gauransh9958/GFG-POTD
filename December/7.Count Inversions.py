class Solution:
    def mergeAndCount(self, arr, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        inv_count = 0
        
        inv_count += self.mergeAndCount(arr, left, mid)
        inv_count += self.mergeAndCount(arr, mid + 1, right)
        
        inv_count += self.merge(arr, left, mid, right)
        
        return inv_count
    
    def merge(self, arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inv_count += (mid - i + 1)
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        for i in range(len(temp)):
            arr[left + i] = temp[i]
        
        return inv_count
    
    def inversionCount(self, arr):
        return self.mergeAndCount(arr, 0, len(arr) - 1)

