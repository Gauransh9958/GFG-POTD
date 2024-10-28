
import java.util.ArrayList;
import java.util.HashSet;


class Solution {
    ArrayList<Integer> removeDuplicate(int arr[]) {
        HashSet<Integer> seen = new HashSet<>();
        ArrayList<Integer> result = new ArrayList<>();

        for (int num : arr) {
            if (!seen.contains(num)) {
                seen.add(num);
                result.add(num);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] arr1 = {2, 2, 3, 3, 7, 5};
        System.out.println(sol.removeDuplicate(arr1)); // Output: [2, 3, 7, 5]

        int[] arr2 = {2, 2, 5, 5, 7, 7};
        System.out.println(sol.removeDuplicate(arr2)); // Output: [2, 5, 7]

        int[] arr3 = {8, 7};
        System.out.println(sol.removeDuplicate(arr3)); // Output: [8, 7]
    }
}
