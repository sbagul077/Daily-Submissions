class Solution {
    public int maxAscendingSum(int[] nums) {
        int result = nums[0];
        int curr = nums[0];

        for(int i = 1; i < nums.length; i++){
            if(nums[i] > nums[i - 1]){
                curr += nums[i];
            }
            else{
                curr = nums[i];
            }
            if(curr > result){
                result = curr;
            }
        }
        return result;
    }
}