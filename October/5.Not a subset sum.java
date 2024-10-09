class Solution {
    public long findSmallest(int[] arr) {
        long smallestMissing = 1; 
        for (int num : arr) {
            if (num > smallestMissing) {
                break;
            }
            smallestMissing += num;
        }

        return smallestMissing;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] arr1 = {1, 2, 3};
        System.out.println("Smallest missing positive integer: " + solution.findSmallest(arr1)); // Output: 7

        int[] arr2 = {3, 6, 9, 10, 20, 28};
        System.out.println("Smallest missing positive integer: " + solution.findSmallest(arr2)); // Output: 1
    }
}
