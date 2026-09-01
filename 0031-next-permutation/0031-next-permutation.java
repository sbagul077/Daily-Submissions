class Solution {
    public void nextPermutation(int[] nums) {
        
        int n = nums.length;
        int i = n - 2;
        while(i >= 0){
            if(nums[i] < nums[i + 1]){
                for(int j = n - 1; j > i; j--){
                    if(nums[j] > nums[i]){
                        swap(nums, i, j);
                        break;
                    }
                }
                break;
            }
            i--;
        }
        reverse(nums, i + 1, n- 1);
    }

    private void swap(int[] nums, int left, int right){

        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

    private void reverse(int[] nums, int start, int end){

        while(start < end){
            swap(nums, start, end);
            start++;
            end--;
        }

    }
}