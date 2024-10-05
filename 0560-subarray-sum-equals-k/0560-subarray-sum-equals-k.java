class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums ==null || nums.length == 0){
            return 0;
        }
        
        int count = 0;
        int currSum = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        map.put(0, 1);
        
        for(int i = 0; i < nums.length; i++){
            currSum += nums[i];
            
            if(map.containsKey(currSum - k)){
                count += map.get(currSum - k);
            }
            
            if(map.containsKey(currSum)){
                map.put(currSum, map.get(currSum) + 1);
            }
            else{
                map.put(currSum ,1);
            }
        }
        return count;
    }
}