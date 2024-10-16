class Solution {
    public int[] productExceptSelf(int[] nums) {
        if(nums == null || nums.length == 0){
            return new int[0];
        }
        
        int[] result = new int[nums.length];
        
        // for(int i = 0; i < nums.length; i++){
        //     nums[i] = 1;
        // }
        
        int rp = 1;
        int temp = 1;
        
        for(int i = 0; i< nums.length; i++){
            rp = rp * temp;            
            result[i] = rp;
            temp = nums[i];
        }
        
        rp = 1;
        temp = 1;
        
        for(int i = nums.length - 1; i >= 0; i--){
            rp = rp * temp;
            result[i] = result[i] * rp;
            temp = nums[i];
        }
        
        return result;            
           
    }
}