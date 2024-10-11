
import java.util.List;


class Solution {
    public List<Integer> rearrange(List<Integer> arr) {
        int n = arr.size();
        
        for (int i = 0; i < n; i++) {
            while (arr.get(i) != -1 && arr.get(i) != i) {
                int tempIndex = arr.get(i);
                if (tempIndex >= 0 && tempIndex < n) {
                    int tempValue = arr.get(tempIndex);
                    arr.set(tempIndex, arr.get(i));
                    arr.set(i, tempValue);
                } else {
                    break;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (arr.get(i) == i) {
                
                continue;
            }
            arr.set(i, -1);
        }

        return arr;
    }
}