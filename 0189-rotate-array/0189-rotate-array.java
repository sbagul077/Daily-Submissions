class Solution {
    public void rotate(int[] nums, int k) {
        if(nums == null || nums.length == 1){
            return;
        }

        int n = nums.length;
        if(k > n){
            k = k % n;
        }
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);

        
    }

    private void reverse(int[] nums, int left, int right){
        
        while(left < right){
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}


// Time Complixty: O(3n)
// Space Complexity: O(1)