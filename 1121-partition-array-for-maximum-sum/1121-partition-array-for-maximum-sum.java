class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        if (arr == null || arr.length == 0)
            return 0;

        int size = arr.length;
        int[] dp = new int[size];
        dp[0] = arr[0];

        for (int i = 1; i < size; i++) {
            int max = arr[i];
            for (int j = 1; j <= k && i - j + 1 >= 0; j++) {
                max = Math.max(max, arr[i - j + 1]);
                if (i - j >= 0) {
                    dp[i] = Math.max(dp[i],max * j + dp[i - j]);
                }else{
                    dp[i] = Math.max(dp[i],max * j);
                }
            }
        }

        return dp[dp.length - 1];

    }
}

//DP
//Time Complexity: O(n * k)
//Space Complexity: O(n)