class Solution {
    public int maxSubArray(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        int result = nums[0];
        int n = nums.length;
        int prev  = Math.max(nums[0], 0);
        for(int i = 1; i < n; i++){

            prev = Math.max(nums[i], prev + nums[i]);
            result = Math.max(result, prev);
        }

        return result;
    }

}

// Time Complexity: O(n)
// Space Complexity: O(1)