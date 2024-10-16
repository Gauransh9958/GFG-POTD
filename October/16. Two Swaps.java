
import java.util.Collections;
import java.util.List;

class Solution {

    public void doOneSwap(int n, List<Integer> arr) {
        for (int i = 0; i < n; i++) {
            if (arr.get(i) != i + 1) {
                for (int j = i + 1; j < n; j++) {
                    if (arr.get(j) == i + 1) {
                        Collections.swap(arr, i, j);
                        return;
                    }
                }
            }
        }
    }

    public boolean checkSorted(List<Integer> arr) {
        int n = arr.size();
        int misMatch = 0;

        for (int i = 0; i < n; i++) {
            if (arr.get(i) != i + 1) misMatch++;
        }

        if (n == 1) return false;
        if (misMatch == 0 || misMatch == 3) return true;

        if (misMatch != 4) return false;

        doOneSwap(n, arr);
        doOneSwap(n, arr);

        for (int i = 0; i < n; i++) {
            if (arr.get(i) != i + 1) return false;
        }
        return true;
}
}