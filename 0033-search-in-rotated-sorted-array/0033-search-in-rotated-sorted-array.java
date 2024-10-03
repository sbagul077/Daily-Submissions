class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0 || nums == null){
            return -1;
        }
        
        int index = 0;
        
        for(int i = 1; i < nums.length; i++){
            if(nums[i] < nums[i - 1]){
                index = i;
                break;
            }
        }
        int low = -1;
        int high = -1;
        if (nums[index] <= target && target <= nums[nums.length - 1]){
             low = index;
             high = nums.length - 1;
        }
        else{
             low = 0;
             high = index - 1;
        }
        
        while (low <= high){
            int mid = low + (high - low) / 2;
            
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] < target){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
    
    return -1;
            
    }
}