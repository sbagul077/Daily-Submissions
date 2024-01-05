class Solution {
    public boolean containsDuplicate(int[] nums) {
        // set = hashset<int>;
        
       Set <Integer> set = new HashSet<Integer>();
        
        // HashMap<Integer, Integer> map = new HashMap<>();
        
        
        for(int i = 0; i< nums.length; i++){
            if(!set.contains(nums[i])){
                set.add(nums[i]);                
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