class Solution {
    public int numIdenticalPairs(int[] nums) {
        int result = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // frequency map
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                result += map.get(nums[i]);
                map.put(nums[i], map.get(nums[i]) + 1);
            }
            else{
                map.put(nums[i], 1);            
            }
        }
        return result;
    }
}

// HashMap
// Time Complexity: O(n)
// Space Complexity: O(n)