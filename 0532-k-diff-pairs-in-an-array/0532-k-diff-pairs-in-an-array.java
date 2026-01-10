class Solution {
    public int findPairs(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        HashSet<List<Integer>> result = new HashSet<>();
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            int complement = nums[i] - k;
            if(map.containsKey(complement) && map.get(complement) != i){
                Integer[] temp = {nums[i], complement};
                Arrays.sort(temp);
                result.add(Arrays.asList(temp));
            }

            complement = nums[i] + k;
            if(map.containsKey(complement) && map.get(complement) != i){
                Integer[] temp = {nums[i], complement};
                Arrays.sort(temp);
                result.add(Arrays.asList(temp));
            }
        }

        return result.size();
    }
}