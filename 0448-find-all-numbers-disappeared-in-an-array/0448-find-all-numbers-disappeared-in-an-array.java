class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList <Integer> result = new ArrayList<>();
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i); 
        }
        
        for(int i = 0; i < nums.length; i++){
            if(!map.containsKey(i + 1)){
                result.add(i + 1);
            }
        }
        return result;
    }
}

// TC : O(2n)
//SC : O(n)