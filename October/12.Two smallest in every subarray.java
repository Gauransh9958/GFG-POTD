

class Solution {
    public int pairWithMaxSum(int[] arr) {
        if (arr.length < 2) {
            return -1;
        }

        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length - 1; i++) {
            int currentSum = arr[i] + arr[i + 1];
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
