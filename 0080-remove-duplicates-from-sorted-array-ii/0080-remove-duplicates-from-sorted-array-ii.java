class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        int count = 1;
        int slow = 1;
        int n = nums.length;

        for(int fast = 1; fast < n; fast++){
            if(nums[fast] == nums[fast - 1]){
                count += 1;
            }else{
                count = 1;
            }

            if(count < 3){
                nums[slow] = nums[fast];
                slow++;
            }
        }

        return slow;
    }
}


//two pointers
// # time complexity: O(n)
// # space complexity: O(1)