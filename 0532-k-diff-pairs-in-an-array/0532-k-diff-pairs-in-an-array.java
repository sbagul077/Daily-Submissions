class Solution {
    public int findPairs(int[] nums, int k) {
        int slow = 0;
        int fast = 1;
        int n = nums.length;
        Arrays.sort(nums);
        int result = 0;

        while(fast < n){
            int curr = nums[fast] - nums[slow];

            if(curr > k){
                slow += 1;
            }
            else if (curr < k || fast == slow){
                fast += 1;
            }
            else{
                result += 1;
                slow++;
                fast++;

                while(fast < n && nums[fast] == nums[fast - 1]){
                    fast += 1;
                }
            }
        }

        return result;
        
    }
}

// #two pointers
// # time complexity: O(nlogn)
// # space complexity: O(1)