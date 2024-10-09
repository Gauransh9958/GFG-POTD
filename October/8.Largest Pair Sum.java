class Solution {
    public static int pairsum(int[] arr) {
        int firstMax = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > firstMax) {
                secondMax = firstMax;
                firstMax = num;
            } else if (num > secondMax) {
                secondMax = num;
            }
        }

        return firstMax + secondMax;
    }
    
    public static void main(String[] args) {
        int[] arr1 = {12, 34, 10, 6, 40};
        System.out.println(pairsum(arr1));

        int[] arr2 = {10, 20, 30};
        System.out.println(pairsum(arr2));
    }
}

