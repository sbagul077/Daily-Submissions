class Solution {
    public int findPairs(int[] nums, int k) {
        Arrays.sort(nums);
        int slow = 0;
        int fast = 1;
        int result = 0;
        int n = nums.length;
        while(fast < n){
            int curr = nums[fast] - nums[slow];
            
            if (curr > k){
                slow++;
            }
            else if(curr < k || slow == fast){
                fast++;
            }else{
                result++;
                slow ++;
                fast++;
                
                while(fast < n && nums[fast] == nums[fast - 1]){
                    fast++;
                }
            }
            
        }
        
        return result;
    }
}