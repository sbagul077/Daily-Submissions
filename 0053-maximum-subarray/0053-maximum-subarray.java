class Solution {
    public int maxSubArray(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        int result = nums[0];
        int rSum = nums[0];

        for(int i = 1; i < nums.length; i++){

            rSum = Math.max(rSum + nums[i], nums[i]);

            result = Math.max(result, rSum);
        }

        return result;
    }
}

//Time Complexity: O(n)
//Space Complexity: O(1)