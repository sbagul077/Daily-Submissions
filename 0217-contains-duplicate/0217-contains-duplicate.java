class Solution {
    public boolean containsDuplicate(int[] nums) {
        // set = hashset<int>;
        
        // HashMap<Integer, Integer> map = new HashMap<>();
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        
        for(int i = 0; i< nums.length; i++){
            if(!map.containsKey(nums[i])){
                map.put(nums[i], nums[i]);                
            }
            else{
                return true;
            }
        }
        
        return false;
        
    }
}


//HashMap
//Time Complexity: O(n)
//Space Complexity: O(n)