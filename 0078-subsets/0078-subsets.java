class Solution {
    
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if(nums == null || nums.length == 0){
            return result;
        }

        result.add(new ArrayList<>());

        for(int i = 0; i < nums.length; i++){
            int size = result.size();
            for(int k = 0; k < size; k++){
                List<Integer> temp = new ArrayList<>(result.get(k));
                temp.add(nums[i]);
                result.add(temp);
            }
        }

        return result;
    }
}

// For Loop
// Time Complexity: O(n^2)
// Space Complexity: O(h)