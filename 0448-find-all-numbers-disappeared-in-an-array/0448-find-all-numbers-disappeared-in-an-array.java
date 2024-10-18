class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList <Integer> result = new ArrayList<>();
        
        
        for(int i = 0; i < nums.length; i++){
            int idx = Math.abs(nums[i]) - 1;
            
            if(nums[idx] > 0){
                nums[idx] *= -1;
            }
        }
        

        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0){
                result.add(i + 1);
            }
        }
        return result;
    }
}

// TC : O(2n)
//SC : O(1)