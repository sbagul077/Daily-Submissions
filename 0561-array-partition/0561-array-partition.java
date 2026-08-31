class Solution {
    public int arrayPairSum(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        Arrays.sort(nums);
        int n = nums.length;

        int minSum = 0;

        for(int i = 0; i < n; i += 2){
            minSum += nums[i];
        }

        return minSum;
    }
}


//Sorting
// Time Compplexity:O(nlogn)
// Space Complexity: O(1)